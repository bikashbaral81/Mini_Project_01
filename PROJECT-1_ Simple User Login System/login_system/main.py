import auth

def menu():
    while True:
        print("\n===== LOGIN SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option (1/2/3): ")

        if choice == '1':            
            auth.register()

        elif choice == '2':
            auth.login()

        elif choice == '3':
            print(" Exiting. Bye!")
            break

        else:
            print(" Invalid choice. Try again.")


menu()
