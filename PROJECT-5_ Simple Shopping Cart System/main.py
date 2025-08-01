from cart import load_cart, add_item, remove_item, view_cart, calculate_total

def main():
    cart = load_cart()

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Show Total Bill")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue

            try:
                price = float(input("Enter item price: ").strip())
                quantity = int(input("Enter quantity: ").strip())
                if price < 0 or quantity <= 0:
                    print("Price must be positive and quantity must be more than zero.")
                    continue
                add_item(cart, name, price, quantity)
                print(f"{quantity} x {name} added to cart.")
            except ValueError:
                print("Invalid input. Enter numeric values for price and quantity.")

        elif choice == "2":
            name = input("Enter item name to remove: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue

            if remove_item(cart, name):
                print(f"{name} removed from cart.")
            else:
                print(f"{name} not found in cart.")

        elif choice == "3":
            view_cart(cart)

        elif choice == "4":
            total, tax, final = calculate_total(cart)
            print(f"\nSubtotal: ₹{total:.2f}")
            print(f"GST (18%): ₹{tax:.2f}")
            print(f"Total Payable: ₹{final:.2f}")

        elif choice == "5":
            print("Thanks for shopping!")
            break

        else:
            print("Invalid choice. Please choose from 1 to 5.")

if __name__ == "__main__":
    main()


