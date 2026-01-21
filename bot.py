import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
import asyncio

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace with your bot token from @BotFather
BOT_TOKEN = '8367542282:AAGC5P1xHjOoRK_HQ4HwBfSYSOZYa1ELYyU'

# Directory to save downloaded videos
DOWNLOAD_DIR = 'downloads'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        '👋 Hello! I can download videos from Instagram, TikTok, and YouTube.\n\n'
        'Just send me a link to the video you want to download!'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        'Send me a link from:\n'
        '• Instagram (posts/reels)\n'
        '• TikTok\n'
        '• YouTube\n\n'
        'I\'ll download and send you the video!'
    )

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Download video from the provided link."""
    url = update.message.text.strip()
    
    # Check if URL is from supported platforms
    supported_platforms = ['instagram.com', 'tiktok.com', 'youtube.com', 'youtu.be']
    if not any(platform in url for platform in supported_platforms):
        await update.message.reply_text(
            '❌ Sorry, I only support Instagram, TikTok, and YouTube links.'
        )
        return
    
    # Send initial message
    status_msg = await update.message.reply_text('⏳ Downloading video...')
    
    try:
        # Configure yt-dlp options
        output_path = os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')
        
        # Special handling for YouTube Shorts - convert to regular URL
        if 'youtube.com/shorts/' in url:
            video_id = url.split('/shorts/')[-1].split('?')[0]
            url = f'https://www.youtube.com/watch?v={video_id}'
        
        ydl_opts = {
            'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': output_path,
            'quiet': False,
            'no_warnings': False,
            'nocheckcertificate': True,
            'extract_flat': False,
            'geo_bypass': True,
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            }
        }
        
        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = await asyncio.to_thread(ydl.extract_info, url, download=True)
            filename = ydl.prepare_filename(info)
        
        # Update status
        await status_msg.edit_text('📤 Uploading video...')
        
        # Check file size (Telegram has a 50MB limit for bots)
        file_size = os.path.getsize(filename)
        if file_size > 50 * 1024 * 1024:  # 50MB in bytes
            await status_msg.edit_text(
                '❌ Video is too large (>50MB). Telegram bots can\'t send files this big.'
            )
            os.remove(filename)
            return
        
        # Send video to user
        with open(filename, 'rb') as video:
            await update.message.reply_video(
                video=video,
                caption=f"✅ Downloaded from {url[:50]}..."
            )
        
        # Delete status message and local file
        await status_msg.delete()
        os.remove(filename)
        
    except Exception as e:
        logger.error(f"Error downloading video: {e}")
        await status_msg.edit_text(
            f'❌ Failed to download video. Error: {str(e)[:100]}'
        )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    
    # Start the bot
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()