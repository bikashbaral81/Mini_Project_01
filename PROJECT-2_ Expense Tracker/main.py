import tracker

def menu():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Choose option (1/2/3/4): ")

        if choice == '1':
            desc = input("Enter expense description: ")
            amt = input("Enter amount (₹): ")
            tracker.add_expense(desc, amt)

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.total_spent()

        elif choice == '4':
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")


menu()
