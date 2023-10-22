# chatBot: A Simple Python Chatbot
# Description
chatBot is a simple chatbot project implemented in Python. It utilizes the ChatterBot library for the core chat functionalities and includes a cleaner utility for preprocessing chat data. The chat data is expected to be provided in a chat.txt file.

## How to Run the Chatbot
To run the chatbot, simply execute the following command:

bash
Copy code
python3 bot.py
Customization
Message Filtering
To add more exceptions in the message filtering process, you can modify the filter_out_msgs tuple in the remove_non_message_text function located in the cleaner.py file.

For example:

python
Copy code
filter_out_msgs = ("<Media omitted>", "Missed voice call", "Your custom exception here")
Providing Chat Data
To train the chatbot, you need to provide chat data in a file named chat.txt.

Requirements
Python 3.x
ChatterBot library
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/chatBot.git
Navigate into the directory:

bash
Copy code
cd chatBot
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run the bot:

bash
Copy code
python3 bot.py

## Author
Geremy

