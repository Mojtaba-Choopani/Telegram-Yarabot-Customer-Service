import json
import requests
from tokenbot import YARABOT_AUTH_TOKEN, YARABOT_API_URL

def forward_to_yarabot(yara_chat_id, user_text, start_new_message):
    # This function forwards the user text to Yarabot and returns the response.
    if start_new_message == 1:
        yara_chat_id = "",
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "authorization": YARABOT_AUTH_TOKEN,  # Use the Yarabot authorization token.
    }
    data = {
        "type": "text",  # Specify the type of content being sent.
        "text": user_text,  # The user query to Yarabot.
        "session_id": yara_chat_id,  # Use the chat ID as the session ID.
    }
    # try:    
    response = requests.post(YARABOT_API_URL, headers=headers, data=data, timeout=10)  # Set a timeout for the request.
    start_new_message = 0
    raw_response = response.content.decode('utf-8')  # Decode the response content    
    messages = ""  # List to hold parsed messages
    for line in raw_response.splitlines():  # Split the response into individual lines
        try:
            json_obj = json.loads(line)  # Parse each line as JSON            
            if "data" in json_obj:
                messages += json_obj["data"] # Extract and store the "data" field
        except json.JSONDecodeError as e:
            print(f"JSON decoding error for line: {line}, Error: {e}")  # Log decoding errors

    if response.status_code == 200:        
        return  "".join(messages)    # response.json().get("data", "Sorry, I couldn't process your request.")  # Return Yarabot's response.
    elif response.status_code == 400:
        return f"Bad Request: Please check your input."
    else:
        return f"An error occurred while contacting Yarabot. Status: {response.status_code}"
