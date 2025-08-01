import json
import os

FILENAME = "cart_data.json"

def load_cart():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}

def save_cart(cart):
    with open(FILENAME, "w") as file:
        json.dump(cart, file, indent=4)

def add_item(cart, name, price, quantity):
    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {"price": price, "quantity": quantity}
    save_cart(cart)

def remove_item(cart, name):
    if name in cart:
        del cart[name]
        save_cart(cart)
        return True
    return False

def view_cart(cart):
    if not cart:
        print("Cart is empty.")
    else:
        print("\nItems in your cart:")
        for item in cart:
            price = cart[item]["price"]
            qty = cart[item]["quantity"]
            print(f"{item}: ₹{price} x {qty}")

def calculate_total(cart):
    total = 0
    for item in cart:
        price = cart[item]["price"]
        qty = cart[item]["quantity"]
        total = total + (price * qty)
    tax = total * 0.18
    final_total = total + tax
    return total, tax, final_total
