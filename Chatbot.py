print()
print("=" * 35)
print("|| 🤖 Welcome to Basic Chatbot ||")
print("=" * 35)
print()


def chatbot():
    while True:
        message = input("You: ")
        if "hello" in message.lower() or "hi" in message.lower():
            print("Chatbot🤖: Hi!\n")

        elif "how are you" in message.lower():
            print("Chatbot🤖: I'm fine, thanks!\n")

        elif "what is your name" in message.lower():
            print("Chatbot🤖: I'm a basic Python chatbot!\n")

        elif "thank you" in message.lower():
            print("Chatbot🤖: You're welcome!\n")

        elif "good morning" in message.lower():
            print("Chatbot🤖: Good morning! ☀️\n")

        elif "good afternoon" in message.lower():
            print("Chatbot🤖: Good afternoon! 🌤️\n")

        elif "good evening" in message.lower():
            print("Chatbot🤖: Good evening! 🌆\n")

        elif "bye" in message.lower():
            print("Chatbot🤖: Goodbye!\n")
            break

        else:
            print("Chatbot🤖: Sorry, I don't understand that.\n")


chatbot()
