print("Welcome to the Chatbot! Type 'bye' to end the conversation.")

while True:
    user_input = input("You: ").lower().strip()
    
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! It's great to chat with you. How can I assist you today?")
    elif user_input in ["how are you", "how r u", "how's it going"]:
        print("Bot: I'm just a program, but I'm here and ready to help! What about you?")
    elif user_input in ["what is your name", "who are you"]:
        print("Bot: My name is ChatBot, and I'm designed to answer simple questions!")
    elif user_input in ["help", "options", "what can you do"]:
        print("Bot: I can chat with you, tell jokes, give weather info, and provide basic information. Try asking something!")
    elif user_input in ["tell me a joke", "joke"]:
        print("Bot: Why did the programmer quit his job? Because he didn't get arrays (a raise)!")
    elif user_input in ["what is the weather like", "weather"]:
        print("Bot: I'm not connected to the internet, but I hope the weather is pleasant where you are!")
    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome! Let me know if there's anything else.")
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day.")
        break
    elif "your creator" in user_input:
        print("Bot: I was created by a human using Python. Want to learn more about Python programming?")
    elif "python" in user_input:
        print("Bot: Python is a powerful, easy-to-learn programming language. Do you have a specific question about Python?")
    else:
        print("Bot: Sorry, I didn't understand that. Could you rephrase your question or try something else?")