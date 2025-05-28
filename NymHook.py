import requests
import json
import time
import threading
from datetime import datetime
import os
import sys
import shutil

class NymHook:
    def __init__(self):
        self.webhook_url = ""
        self.webhook_name = ""
        self.colors = {
            "red": 0xff0000,
            "green": 0x00ff00,
            "blue": 0x0000ff,
            "yellow": 0xffff00,
            "purple": 0x800080,
            "orange": 0xffa500,
            "pink": 0xffc0cb,
            "cyan": 0x00ffff,
            "white": 0xffffff,
            "black": 0x000000
        }
        self.set_title()
        self.setup_webhook()
    
    def set_title(self):
        """Set CMD window title"""
        if os.name == 'nt':
            os.system('title NymHook v2.0 - Discord Webhook Multi-Tool')
        else:  # Linux/Mac
            sys.stdout.write('\33]0;NymHook v2.0 - Discord Webhook Multi-Tool\a')
            sys.stdout.flush()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def rgb(self, r, g, b): 
        return f"\033[38;2;{r};{g};{b}m"

    def generate_gradient(self, text):
        dark_blue = (20, 40, 120)    
        white = (255, 255, 255)      
        
        result = ""
        for i, char in enumerate(text):
            ratio = i / max(len(text) - 1, 1)
            
            r = int(dark_blue[0] + (white[0] - dark_blue[0]) * ratio)
            g = int(dark_blue[1] + (white[1] - dark_blue[1]) * ratio)
            b = int(dark_blue[2] + (white[2] - dark_blue[2]) * ratio)
            
            result += self.rgb(r, g, b) + char
        return result + "\033[0m"

    def print_centered(self, text):
        term_width = shutil.get_terminal_size().columns
        spaces = (term_width - len(text)) // 2
        if spaces > 0:
            print(" " * spaces + self.generate_gradient(text))
        else:
            print(self.generate_gradient(text))
    
    def print_left(self, text):
        print(self.generate_gradient(text))
    
    def setup_webhook(self):
        """Webhook setup beim Start"""
        self.clear_screen()
        self.print_centered("NymHook v2.0 - Setup")
        print("\n")
        self.print_left("Enter Webhook URL:")
        
        while True:
            self.webhook_url = input("> ")
            if self.validate_webhook():
                self.print_left("✓ Webhook URL successfully set!")
                break
            else:
                self.print_left("✗ Invalid Webhook URL! Please try again:")
    
    def validate_webhook(self):
        if not self.webhook_url:
            return False
        try:
            response = requests.get(self.webhook_url)
            if response.status_code == 200:
                data = response.json()
                self.webhook_name = data.get('name', 'Unknown Webhook')
                return True
            return False
        except:
            return False
    
    def print_banner(self):
        ascii_art = [
            "███╗   ██╗██╗   ██╗███╗   ███╗██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗",
            "████╗  ██║╚██╗ ██╔╝████╗ ████║██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝",
            "██╔██╗ ██║ ╚████╔╝ ██╔████╔██║███████║██║   ██║██║   ██║█████╔╝ ",
            "██║╚██╗██║  ╚██╔╝  ██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██╔═██╗ ",
            "██║ ╚████║   ██║   ██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║  ██╗",
            "╚═╝  ╚═══╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝"
        ]
        
        print("\n\n")
        
        for line in ascii_art:
            self.print_centered(line)
        
        print("\n")
        self.print_centered("Discord Webhook Multi-Tool v2.0")
        self.print_centered("Created by NymTools")
        print("\n")
        
        if self.webhook_name:
            self.print_centered(f"Logged in: {self.webhook_name}")
        print("\n")
    
    def show_menu(self):
        menu_items = [
            "[1] Send Embed",
            "[2] Spam Webhook", 
            "[3] Delete Webhook",
            "[4] Show Webhook Info",
            "[5] Send File",
            "[6] Color Test",
            "[0] Exit"
        ]
        
        self.print_centered("MAIN MENU")
        print()
        
        for item in menu_items:
            self.print_left(item)
        
        print()
    
    def send_embed(self):
        self.print_left("Create Embed:")
        
        title = input("Title: ")
        description = input("Description: ")
        
        self.print_left("Available colors:")
        
        for color_name in self.colors.keys():
            self.print_left(f"- {color_name}")
        
        color_input = input("Choose color: ").lower()
        color = self.colors.get(color_input, 0x0099ff)
        
        embed = {
            "title": title,
            "description": description,
            "color": color,
            "timestamp": datetime.utcnow().isoformat(),
            "footer": {
                "text": "NymHook v2.0"
            }
        }
        
        data = {"embeds": [embed]}
        
        try:
            response = requests.post(self.webhook_url, json=data)
            if response.status_code == 204:
                self.print_left("✓ Embed sent successfully!")
            else:
                self.print_left(f"✗ Error sending embed: {response.status_code}")
        except Exception as e:
            self.print_left(f"✗ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def spam_webhook(self):
        self.print_left("⚠️  WARNING: Spamming can lead to rate limits!")
        
        confirm = input("Continue? (yes/no): ").lower()
        
        if confirm not in ["yes", "y"]:
            return
        
        message = input("Spam message: ")
        count = int(input("Amount: "))
        delay = float(input("Delay (seconds): "))
        
        self.print_left("Spam started...")
        
        for i in range(count):
            try:
                data = {"content": message} 
                response = requests.post(self.webhook_url, json=data)
                
                if response.status_code == 204:
                    self.print_left(f"✓ Message {i+1}/{count} sent")
                else:
                    self.print_left(f"✗ Error at message {i+1}: {response.status_code}")
                
                time.sleep(delay)
            except Exception as e:
                self.print_left(f"✗ Error: {str(e)}")
                break
        
        input("\nPress Enter to continue...")
    
    def delete_webhook(self):
        self.print_left("⚠️  WARNING: Webhook will be permanently deleted!")
        
        confirm = input("Really delete? (yes/no): ").lower()
        
        if confirm not in ["yes", "y"]:
            return
        
        try:
            response = requests.delete(self.webhook_url)
            if response.status_code == 204:
                self.print_left("✓ Webhook deleted successfully!")
                self.webhook_url = ""
                self.webhook_name = ""
            else:
                self.print_left(f"✗ Error deleting webhook: {response.status_code}")
        except Exception as e:
            self.print_left(f"✗ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def webhook_info(self):
        try:
            response = requests.get(self.webhook_url)
            if response.status_code == 200:
                data = response.json()
                self.print_left("Webhook Information:")
                
                self.print_left(f"Name: {data.get('name', 'N/A')}")
                self.print_left(f"ID: {data.get('id', 'N/A')}")
                self.print_left(f"Guild ID: {data.get('guild_id', 'N/A')}")
                self.print_left(f"Channel ID: {data.get('channel_id', 'N/A')}")
                self.print_left(f"Token: {data.get('token', 'N/A')[:10]}...")
            else:
                self.print_left("✗ Error retrieving webhook information")
        except Exception as e:
            self.print_left(f"✗ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def send_file(self):
        self.print_left("Enter file path:")
        file_path = input("> ")
        
        if not os.path.exists(file_path):
            self.print_left("✗ File not found!")
            input("\nPress Enter to continue...")
            return
        
        try:
            with open(file_path, 'rb') as file:
                files = {'file': file}
                response = requests.post(self.webhook_url, files=files)
                
                if response.status_code == 200:
                    self.print_left("✓ File sent successfully!")
                else:
                    self.print_left(f"✗ Error sending file: {response.status_code}")
        except Exception as e:
            self.print_left(f"✗ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def color_test(self):
        self.print_left("Color Test - Available Colors:")
        
        self.print_left("GRADIENT DEMO")
        
        self.print_left("Rainbow Examples:")
        self.print_left("Red to Orange: Beautiful color transition example")
        self.print_left("Orange to Yellow: Beautiful color transition example")
        self.print_left("Yellow to Green: Beautiful color transition example")
        self.print_left("Green to Cyan: Beautiful color transition example")
        self.print_left("Cyan to Blue: Beautiful color transition example")
        self.print_left("Blue to Purple: Beautiful color transition example")
        
        self.print_left("Available Embed Colors:")
        
        color_demos = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]
        
        for color_name in color_demos:
            self.print_left(f"■ {color_name.upper()}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        while True:
            self.clear_screen()
            self.print_banner()
            self.show_menu()
            
            try:
                self.print_left("Choose an option:")
                choice = input("> ")
                
                if choice == "1":
                    self.send_embed()
                elif choice == "2":
                    self.spam_webhook()
                elif choice == "3":
                    self.delete_webhook()
                elif choice == "4":
                    self.webhook_info()
                elif choice == "5":
                    self.send_file()
                elif choice == "6":
                    self.color_test()
                elif choice == "0":
                    self.print_left("Goodbye! Thanks for using NymHook!")
                    break
                else:
                    self.print_left("✗ Invalid selection!")
                    input("\nPress Enter to continue...")
            except KeyboardInterrupt:
                self.print_left("\n\nGoodbye! Thanks for using NymHook!")
                break
            except Exception as e:
                self.print_left(f"✗ Unexpected error: {str(e)}")
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        tool = NymHook()
        tool.run()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        input("Press Enter to exit...")