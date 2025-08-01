import os

FILE_NAME = "PROJECT-1_Simple User Login System/login_system/users.txt"

def register():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as f:
                for line in f:
                    user = line.strip().split(',')[0]
                    if user == username:
                        print(" Username already exists.")
                        return

        with open(FILE_NAME, 'a') as f:
            f.write(f"{username},{password}\n")
        print(" Registered successfully.")
    
    except Exception as e:
        print(" Error during registration:", e)

def login():
    try:
        username_input = input("Enter username: ")
        with open(FILE_NAME, 'r') as f:
            found = False
            stored_password = None
            for line in f:
                user, pwd = line.strip().split(',')
                if user == username_input:
                    found = True
                    stored_password = pwd
                    break

            if found:
                password_input = input("Enter your password: ")
                if password_input == stored_password:
                    print(f"Welcome, {username_input}!")
                else:
                    print("Incorrect password.")
            else:
                print("Username not found.")

    except FileNotFoundError:
        print("No users registered yet.")
    
    except Exception as e:
        print("Error during login:", e)


