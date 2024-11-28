# In-memory user storage
users = {}

# Function for registration
def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

# Function for login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

# Function to start the quiz
def start_quiz():
    print("Welcome to the Quiz!")
    questions = {
        "Which of the following keywords is used to define a function in Python? : ": "def",
        "which loop is used when number of iteration unknown ? : ": "while loop",
        "which technique is used for quick sort ? : ": "divide and conqure",
        "when we don't give any argument ina function then it is called : ": "default argument",
        "The function which call itself is called : ": "recursion",
    } 
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was:", answer)
    print(f"Your final score is {score}/{len(questions)}")

# Main function to run the application
def main():
    while True:
        print("\nWelcome to the Quiz Application!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                start_quiz()
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

