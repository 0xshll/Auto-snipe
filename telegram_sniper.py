from telethon import TelegramClient, events, connection
from telethon.tl.functions.messages import ForwardMessagesRequest
import asyncio
import os
import platform
import sys
from dotenv import load_dotenv
from colorama import init, Fore, Back, Style
import time
import logging

# Initialize colorama
init()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clear_screen():
    """Clear screen based on OS"""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_welcome():
    # Clear screen
    clear_screen()
    
    # ASCII art for the welcome message
    welcome_art = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════════╗
║                                                                ║
║  {Fore.YELLOW}██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗{Fore.CYAN}  ║
║  {Fore.YELLOW}██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║{Fore.CYAN}  ║
║  {Fore.YELLOW}██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║{Fore.CYAN}  ║
║  {Fore.YELLOW}██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║{Fore.CYAN}  ║
║  {Fore.YELLOW}╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║{Fore.CYAN}  ║
║  {Fore.YELLOW} ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝{Fore.CYAN}  ║
║                                                                ║
║  {Fore.GREEN}Welcome to the Telegram Channel Post Sniper!{Fore.CYAN}              ║
║  {Fore.GREEN}Made by Yasser{Fore.CYAN}                                        ║
║  {Fore.GREEN}Telegram: @yyeir{Fore.CYAN}                                      ║
║                                                                ║
╚════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(welcome_art)
    time.sleep(2)  # Pause for 2 seconds to let users read the welcome message

def check_requirements():
    """Check if all required packages are installed"""
    required_packages = ['telethon', 'python-dotenv', 'colorama']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"{Fore.YELLOW}Installing missing packages: {', '.join(missing_packages)}{Style.RESET_ALL}")
        os.system(f"{sys.executable} -m pip install {' '.join(missing_packages)}")

def main():
    # Check and install requirements
    check_requirements()
    
    # Load environment variables
    load_dotenv()
    
    # Print welcome message
    print_welcome()
    
    # Telegram API credentials
    API_ID = input(f"{Fore.CYAN}Please enter your API ID: {Style.RESET_ALL}")
    API_HASH = input(f"{Fore.CYAN}Please enter your API Hash: {Style.RESET_ALL}")
    
    # Initialize the client with optimized settings
    client = TelegramClient(
        'sniper_session',
        API_ID,
        API_HASH,
        connection=connection.ConnectionTcpFull,
        connection_retries=5,
        retry_delay=1,
        auto_reconnect=True,
        timeout=30,
        receive_updates=True
    )
    
    # Store the sniper bot username
    SNIPER_BOT = None
    
    # Store the channels to monitor
    MONITORED_CHANNELS = []
    
    # Create a semaphore to limit concurrent operations
    semaphore = asyncio.Semaphore(10)  # Allow up to 10 concurrent operations
    
    async def forward_message(event):
        async with semaphore:  # Limit concurrent operations
            try:
                # Forward the message to the sniper bot
                await client(ForwardMessagesRequest(
                    from_peer=event.chat_id,
                    id=[event.message.id],
                    to_peer=SNIPER_BOT,
                    silent=True,  # Don't notify the user
                    background=True  # Don't wait for the message to be sent
                ))
                print(f"{Fore.GREEN}✓ Forwarded message from {event.chat.title}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}✗ Error forwarding message: {str(e)}{Style.RESET_ALL}")
    
    async def start_bot():
        # Start the client with optimized settings
        await client.start()
        
        # Get the sniper bot username
        nonlocal SNIPER_BOT
        SNIPER_BOT = input(f"{Fore.CYAN}Please enter the sniper bot username (without @): {Style.RESET_ALL}")
        
        # Get channels to monitor
        print(f"\n{Fore.CYAN}Enter the channels to monitor (one per line, without @). Press Enter twice when done:{Style.RESET_ALL}")
        while True:
            channel = input()
            if not channel:
                break
            MONITORED_CHANNELS.append(channel)
        
        print(f"\n{Fore.GREEN}Bot is now running and monitoring channels...{Style.RESET_ALL}")
        
        # Set up event handler for new messages with optimized settings
        @client.on(events.NewMessage(chats=MONITORED_CHANNELS))
        async def handler(event):
            # Create a task for forwarding to avoid blocking
            asyncio.create_task(forward_message(event))
        
        # Keep the script running
        await client.run_until_disconnected()
    
    # Run the main function
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Bot stopped by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")

if __name__ == '__main__':
    main() 