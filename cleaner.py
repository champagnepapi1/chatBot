#!/usr/bin/env python3
import re

# Remove metadata like timestamps and usernames from chat log
def remove_chat_metadata(chat_export_file):
    try:
        # Regular expressions to capture various parts of a chat metadata line
        date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"
        dash_whitespace = r"\s-\s"
        username = r"([\w\s]+)"
        metadata_end = r":\s"
        pattern = date_time + dash_whitespace + username + metadata_end

        with open(chat_export_file, "r") as corpus_file:
            content = corpus_file.read()
    except FileNotFoundError:
        print("File not found.")
        return None
    
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))

# Remove lines containing non-message text from the chat log
def remove_non_message_text(export_text_lines):
    if export_text_lines is None:
        return None

    messages = export_text_lines[1:-1]
    #Here you can write what you want to omit in the filtering process
    filter_out_msgs = ()
    return tuple((msg for msg in messages if msg not in filter_out_msgs))

# Write the cleaned messages back to a file
def write_cleaned_corpus_to_file(cleaned_corpus, filename):
    if cleaned_corpus is None:
        print("Nothing to write.")
        return None
    
    with open(filename, 'w') as f:
        for line in cleaned_corpus:
            f.write(f"{line}\n")
            
# Orchestrates the process of cleaning the chat log and saving it
def cleaner():
    message_corpus = remove_chat_metadata("Chat.txt")
    cleaned_corpus = remove_non_message_text(message_corpus)
    if cleaned_corpus:
        write_cleaned_corpus_to_file(cleaned_corpus, "Cleaned_Chat.txt")
        return cleaned_corpus
    else:
        print("Cleaning process failed.")
        return None

if __name__ == "__main__":
    result = cleaner()
    if result:
        print("Cleaning and writing process completed successfully.")
    else:
        print("Cleaning and writing process failed.")
