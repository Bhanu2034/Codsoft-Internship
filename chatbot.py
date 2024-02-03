import random

def simple_chatbot(user_input):
    # Predefined rules
    rules = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "bye": "Goodbye! Have a great day.",
        "your name": "I'm a chatbot, you can call me ChatGPT.",
        # Add more rules as needed
    }

    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()

    # Check if user input matches any predefined rule
    for key, value in rules.items():
        if key in user_input:
            return value

    # Random responses for certain inputs
    if "joke" in user_input:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!", "I told my wife she should embrace her mistakes. She gave me a hug."]
        return random.choice(jokes)

    # Check if the user asked a question
    if "?" in user_input:
        return "I'm not sure, what do you think?"

    # If no match found, default response
    return "I'm not sure how to respond to that. Ask me something else."

# Example usage
print("Chatbot: Hi there! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
