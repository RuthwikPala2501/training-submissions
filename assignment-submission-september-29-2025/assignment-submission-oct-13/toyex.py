# List - items in the cart
cart = ["apple", "banana", "apple", "milk"]

# Dictionary - price of each item
prices = {"apple": 1.5, "banana": 0.8, "milk": 2.0}

# Set - to show unique items
unique_items = set(cart)

# Tuple - store customer info (fixed)
customer = ("Ruthwik", "Bensalem")

# Calculate total bill
total = sum(prices[item] for item in cart)

print("Customer:", customer)
print("Items in cart:", cart)
print("Unique items:", unique_items)
print("Total Bill: $", total)

