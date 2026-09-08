"""
CodeAlpha - Python Programming Internship
Task 4: Basic Chatbot

A simple rule-based chatbot that responds to predefined
greetings and phrases using if-elif logic.
"""


def get_response(user_input):
    """Return a predefined reply based on keywords in the user's input."""
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
    
    if any(word in text for word in ["good", "great", "awesome", "fantastic"]):
        return "That's good to hear!"

    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif "your name" in text:
        return "I'm a simple chatbot built for the CodeAlpha internship."

    elif "what can you do" in text or "help" in text:
        return "I can chat about basic things! Try saying hello, asking how I am, or say bye to exit."

    elif "thank" in text:
        return "You're welcome!"

    elif text in ["bye", "goodbye", "exit", "quit", "see you", "later","talk to you later"]:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


def run_chatbot():
    print("Chatbot: Hi! Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    run_chatbot()