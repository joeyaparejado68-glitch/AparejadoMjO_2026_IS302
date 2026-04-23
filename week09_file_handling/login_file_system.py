def register_account():
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    with open("users.txt", "a") as file_store:
        file_store.write(username_input + "," + password_input + "\n")

    print("User registered successfully\n")


def login_account():
    user_login = input("Enter username: ")
    pass_login = input("Enter password: ")

    with open("users.txt", "r") as file_reader:
        for record in file_reader:
            stored_user, stored_pass = record.strip().split(",")

            if user_login == stored_user and pass_login == stored_pass:
                print("Login successful\n")
                return

    print("Invalid username or password\n")


while True:
    print("1 Register")
    print("2 Login")
    print("3 Exit")

    choice_input = input("Choose option: ")

    if choice_input == "1":
        register_account()
    elif choice_input == "2":
        login_account()
    elif choice_input == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again\n")