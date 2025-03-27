import requests  # Import the requests library to make HTTP requests.
import json
from tokenbot import BASE_URL, YARABOT_API_URL, YARABOT_AUTH_TOKEN
from send_update import send_message, get_updates
from yara import forward_to_yarabot

start_new_message = 0,
yara_chat_id = "",

def main():
    """
    Main function to run the bot.
    """
    offset = None  # Start processing updates from the beginning
    while True:
        updates = get_updates(offset)  # Fetch updates from Telegram API
        if not updates:
            continue  # No new updates, continue looping

        for update in updates:
            offset = update["update_id"] + 1  # Update the offset

            # Check if the update contains a message
            if "message" in update:
                chat_id = update["message"]["chat"]["id"]
                text = update["message"].get("text", "")

                if text == "/start":
                    send_message(chat_id, "سلام من قراره برای مدیریت پاسخ مشتریان کمکت کنم. ازم بپرس تا باهام آشنا بشی")
                    # send_inline_keyboard(chat_id)
                    start_new_message = 1                    
                else:                    
                    response = forward_to_yarabot(yara_chat_id=yara_chat_id, user_text=text, start_new_message=0)  # Forward the text to Yarabot.
                    send_message(chat_id, response)  # Send the Yarabot response back to the user.
            
if __name__ == "__main__":  # Check if the script is being run directly.
    main()  # Call the main function to start the bot.    