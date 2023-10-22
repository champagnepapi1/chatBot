from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import cleaner  # Importing the cleaner function from cleaner.py

# Initialize the ChatBot object
chatbot = ChatBot("Chatpot")

# Clean the chat data with the cleaner function and train the chatbot
try:
    cleaned_data = cleaner()
    if cleaned_data is not None:
        print("Cleaned data successfully!", cleaned_data)
        trainer = ListTrainer(chatbot)
        trainer.train(cleaned_data)
    else:
        print("Failed to clean data.")
except Exception as e:
    print(f"An error occurred: {e}")

# Predefined responses for training
trainer.train([
    "Hi",
    "Welcome, friend 👋"
])

trainer.train([
    "Are you the moon?",
    "No, I'm a chatbot 🌛"
])

# Loop to continue the conversation until an exit condition is met
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        print("Exiting chatbot.")
        break
    else:
        print(f"🌛 {chatbot.get_response(query)}")
