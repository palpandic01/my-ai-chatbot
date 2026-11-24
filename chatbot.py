import random

print("=" * 40)
print("       PALPANDI AI CHATBOT")
print("=" * 40)
print("Hello! I'm your chatbot.")
print("Type 'bye' to exit.\n")

responses = {
    "hello": [
        "Hello! How are you?",
        "Hi there! Nice to meet you.",
        "Hey! How can I help you?"
    ],
    "hi": [
        "Hi!",
        "Hello!",
        "Hey there!"
    ],
    "how are you": [
        "I'm doing great! Thanks for asking.",
        "I'm fine. How are you?",
        "I'm ready to chat with you!"
    ],
    "your name": [
        "I'm Palpandi's AI Chatbot.",
        "You can call me Python Bot!"
    ],
    "python": [
        "Python is a popular programming language.",
        "Python is great for AI, automation, and web development."
    ],
    "ai": [
        "AI stands for Artificial Intelligence.",
        "AI helps computers perform tasks that normally require human intelligence."
    ],
    "help": [
        "You can ask me about Python, AI, or just say hello!"
    ]
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    found_response = False

    for keyword, reply_list in responses.items():
        if keyword in user_input:
            print("Bot:", random.choice(reply_list))
            found_response = True
            break

    if not found_response:
        print("Bot: Sorry, I don't understand that yet.")
        print("Try asking me about Python, AI, or say hello!")
