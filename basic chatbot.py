def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if "hello" in user:
            print("Chatbot: Hi there!")
        elif "how are you" in user:
            print("Chatbot: I'm fine, thanks for asking!")
        elif "bye" in user:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()

