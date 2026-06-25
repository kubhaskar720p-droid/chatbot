from datetime import datetime
import random

user_name = ""

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python developer go broke? Because he used up all his cache!",
    "Debugging: Being the detective in a crime movie where you are also the criminal."
]

print("=" * 50)
print("🤖 SHADOW MINI CHATBOT")
print("Type 'help' to see commands")
print("Type 'bye' to exit")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user == "your name":
        print("Bot: My name is Shadow Mini Bot.")

    elif user == "my name":
        if user_name:
            print(f"Bot: Your name is {user_name}.")
        else:
            print("Bot: I don't know your name yet.")

    elif user.startswith("name "):
        user_name = user[5:]
        print(f"Bot: Nice to meet you, {user_name}!")

    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    elif user == "joke":
        print("Bot:", random.choice(jokes))

    elif user == "calc":
        try:
            num1 = float(input("First number: "))
            op = input("Operator (+ - * /): ")
            num2 = float(input("Second number: "))

            if op == "+":
                print("Result =", num1 + num2)
            elif op == "-":
                print("Result =", num1 - num2)
            elif op == "*":
                print("Result =", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Result =", num1 / num2)
                else:
                    print("Cannot divide by zero")
            else:
                print("Invalid operator")
        except:
            print("Invalid input")

    elif user == "help":
        print("""
Available Commands:
hello
how are you
your name
name <your_name>
my name
time
date
joke
calc
help
bye
""")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")