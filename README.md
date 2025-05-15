# Telegram Channel Post Sniper

A fast and efficient Telegram bot that monitors channels and forwards new posts to a sniper bot instantly.

## Features

- 🚀 Ultra-fast message forwarding
- 🔄 Automatic package installation
- 🌈 Beautiful colored interface
- 📱 Works on Windows, Linux, Android (Termux), and macOS
- 🔒 Secure session management
- ⚡ Concurrent message handling

## Installation

### Windows
```bash
# Install Python 3.11 or later
# Download from https://www.python.org/downloads/

# Clone the repository
git clone https://github.com/yourusername/telegram-sniper.git
cd telegram-sniper

# Run the script
python telegram_sniper.py
```

### Linux/macOS
```bash
# Install Python
sudo apt update
sudo apt install python3 python3-pip  # For Ubuntu/Debian
# OR
brew install python3  # For macOS

# Clone the repository
git clone https://github.com/yourusername/telegram-sniper.git
cd telegram-sniper

# Run the script
python3 telegram_sniper.py
```

### Android (Termux)
```bash
# Install Termux from F-Droid
# Open Termux and run:
pkg update
pkg install python git
git clone https://github.com/yourusername/telegram-sniper.git
cd telegram-sniper
python telegram_sniper.py
```

## Usage

1. Get your Telegram API credentials:
   - Go to https://my.telegram.org/auth
   - Log in with your phone number
   - Go to 'API development tools'
   - Create a new application
   - Copy the `api_id` and `api_hash`

2. Run the script and follow the prompts:
   - Enter your API ID
   - Enter your API Hash
   - Enter your phone number when asked
   - Enter the verification code sent to your Telegram account
   - Enter the sniper bot username (without @)
   - Enter the channels to monitor (one per line, without @)
   - Press Enter twice when done entering channels

## Requirements

The script will automatically install these requirements:
- telethon==1.28.5
- python-dotenv==1.0.0
- colorama==0.4.6

## Notes

- Make sure you have the necessary permissions to forward messages from the channels you're monitoring
- The script creates a session file (`sniper_session`) to maintain your login state
- You can stop the script at any time by pressing Ctrl+C

## Author

- Yasser
- Telegram: @yyeir

## License

This project is licensed under the MIT License - see the LICENSE file for details. 