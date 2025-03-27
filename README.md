# Telegram Yarabot Customer Service Bot

## Description
This repository contains the source code for a Telegram bot designed to manage customer service interactions by integrating with Yarabot. The bot is capable of forwarding user messages to Yarabot and displaying the responses back to the user, making it a dynamic tool for real-time customer support.

## Features
- Fetch and process updates from Telegram.
- Forward user queries to Yarabot.
- Handle different types of user interactions, starting with a welcome message.

## Components
The project consists of three main Python scripts:
- `main.py`: The main script that runs the bot, processing Telegram updates and coordinating responses.
- `send_update.py`: Contains functions to interact with the Telegram API, including fetching updates and sending messages.
- `yara.py`: Manages communication between the Telegram bot and Yarabot, including forwarding texts and handling responses.

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Telegram-Yarabot-Customer-Service.git
