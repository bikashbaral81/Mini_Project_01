import os

FILE_NAME = "ass/miniProject2/expense_tracker/expenses.txt"

def add_expense(description, amount):
    try:
        amount = float(amount)
        if amount <= 0:
            print(" Amount must be positive.")
            return
        with open(FILE_NAME, 'a') as f:
            f.write(f"{description},{amount}\n")
        print(" Expense added.")
    except ValueError:
        print(" Invalid amount. Must be a number.")
    except Exception as e:
        print(" Error while adding expense:", e)

def view_expenses():
    try:
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()
            if not lines:
                print(" No expenses found.")
                return
            print("\n Expenses:")
            for line in lines:
                desc, amt = line.strip().split(',')
                print(f"- {desc}: ₹{amt}")
    except FileNotFoundError:
        print(" No expenses file found.")
    except Exception as e:
        print("Error reading file:", e)

def total_spent():
    try:
        total = 0.0
        with open(FILE_NAME, 'r') as f:
            for line in f:
                _, amt = line.strip().split(',')
                total += float(amt)
        print(f" Total Spent: ₹{total}")
    except FileNotFoundError:
        print(" No expenses file found.")
    except Exception as e:
        print(" Error calculating total:", e)
