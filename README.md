# 🎬 Vidmate

A powerful Telegram bot that downloads videos from Instagram, TikTok, and YouTube directly to your chat. Perfect for video editors who need quick access to social media content.

## ✨ Features

- 📥 Download videos from multiple platforms
  - Instagram (Posts & Reels)
  - TikTok
  - YouTube (Videos & Shorts)
- 🚀 Fast and reliable downloads
- 📱 Direct delivery to Telegram
- 🎯 Simple to use - just send a link
- 🔒 Private bot for personal use

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- FFmpeg (required for YouTube video processing)
- pip (Python package manager)

### Installing FFmpeg

**Windows:**
```bash
choco install ffmpeg
```
Or download from [ffmpeg.org](https://ffmpeg.org/download.html)

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## 📦 Installation

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd vidmate
   ```

2. **Install Python dependencies**
   ```bash
   pip install python-telegram-bot yt-dlp
   ```

3. **Create your Telegram bot**
   - Open Telegram and search for `@BotFather`
   - Send `/newbot` command
   - Follow the instructions to choose a name and username
   - Copy the bot token you receive

4. **Configure the bot**
   - Open the `bot.py` file
   - Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token:
     ```python
     BOT_TOKEN = 'your_actual_token_here'
     ```

## 🚀 Usage

1. **Start the bot**
   ```bash
   python bot.py
   ```
   You should see: `Bot is running...`

2. **Open your bot in Telegram**
   - Search for your bot by the username you created
   - Send `/start` to begin

3. **Download videos**
   - Simply send any video link from Instagram, TikTok, or YouTube
   - The bot will download and send the video back to you
   - Wait for the upload to complete

## 💡 Commands

- `/start` - Initialize the bot and see welcome message
- `/help` - Display supported platforms and usage instructions

## ⚙️ Configuration

### Download Directory
By default, videos are temporarily saved in a `downloads` folder. You can change this in the code:
```python
DOWNLOAD_DIR = 'downloads'  # Change to your preferred path
```

### File Size Limit
Telegram bots have a 50MB upload limit. Videos larger than this will not be sent.

## 🔧 Troubleshooting

### YouTube Shorts not downloading
Make sure you have:
- Updated yt-dlp: `pip install --upgrade yt-dlp`
- Installed FFmpeg properly
- Stable internet connection

### Bot not responding
- Check if the bot token is correct
- Ensure the bot is running (`python bot.py`)
- Verify your internet connection

### "Failed to download video" error
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Check if the video URL is valid and accessible
- Some private or age-restricted content may not be downloadable

## 📝 Notes

- The bot automatically deletes downloaded files after sending to save disk space
- Only works with public videos (private accounts may not work)
- Download speed depends on your internet connection and video size
- This is intended for personal use only - respect copyright and platform terms of service

## 🔄 Keeping Updated

To ensure the bot works with the latest platform changes:

```bash
pip install --upgrade yt-dlp python-telegram-bot
```

Run this command periodically, especially if downloads start failing.

## 📄 License

This project is for personal use. Please respect copyright laws and terms of service of the platforms you're downloading from.

## 🤝 Contributing

This is a personal project, but feel free to fork and modify for your own needs!

## ⚠️ Disclaimer

This bot is intended for personal use only. Users are responsible for ensuring their use complies with:
- Platform terms of service
- Copyright laws
- Fair use guidelines

Always obtain proper permissions before using downloaded content commercially.

---

Made with ❤️ for video editors who need quick access to social media content.
