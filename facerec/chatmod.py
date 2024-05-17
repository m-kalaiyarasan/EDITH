import nltk
import random

# Example conversation pairs
conversations = [
    ("Hello", "Hi there!"),
    ("How are you?", "I'm fine, thank you."),
    ("What's your name?", "My name is ChatBot."),
    ("whats going on", "nothing sir"),
    # Add more conversation pairs as needed
]

# Preprocess data
def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return tokens

# Response generation function
def generate_response(user_input):
    user_input_tokens = preprocess(user_input)
    for pattern, response in conversations:
        pattern_tokens = preprocess(pattern)
        if set(pattern_tokens).intersection(user_input_tokens):
            return response
    return "I'm sorry, I don't understand."

# Main interaction loop
if __name__ == "__main__":
    print("Type 'quit' to exit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = generate_response(user_input)
        print(f"Bot: {response}")
