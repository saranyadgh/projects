def respond(input_text):
    input_text = input_text.lower()
    if "hello" in input_text:
        return "Hi there! How can I assist you today?"
    elif "how are you" in input_text:
        return "I'm just a bot, but thanks for asking!"
    elif "what internship am i doing?" in input_text:
        return "Your'e now an Codsoft Intern"
    elif "bye" in input_text:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Welcome to the simple chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(respond(user_input))
            break
        else:
            print("Bot:", respond(user_input))

if __name__ == "__main__":
    main()
