"""""""""""""""""""""""""""""""""
"    C2C Elite 101 - Prework    "
"            Chatbox            "
"         Emily Bedolla         "
"""""""""""""""""""""""""""""""""

# welcomes the user
print("\nWelcome to the Elite 101 Chatbot!\n\n")

# collects the user's name and age
name = input("What is your name? ")
age = input("Hello, " + name + ", what is your age? ")

# asks the user how it can help them
print("Welcome " + name + "! How can I help you today?\n")
print("Please choose from the following options:\n1. Placeholder Option 1\n2. Placeholder Option 2\n3. Placeholder Option 3\n4. Exit the conversation")

# allows the user to choose from a list of options on how they can continue the conversation
userChoice = input("\nEnter the number of your choice: ")

# while loop to keep checking what the user's choice is and executing the appropriate code until the user inputs "4" to exit
while userChoice != "4":
    if userChoice == "1":
        # action1
        print()
    elif userChoice == "2":
        # action2
        print()
    elif userChoice == "3":
        # action3
        print()
    else:
        print("That is not a valid choice. Please, try again.")
    userChoice = input("\nEnter the number of your choice: ")

# goodbye message
print("\nGoodbye, " + name + " Have a great day!\n\n")