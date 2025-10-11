# Small dataset (only 2 orders)
orders = [
    {"customer": "Roy", "product": "Notebook", "qty": 2, "price": 4.5},
    {"customer": "Wick", "product": "Marker", "qty": 3, "price": 2.0}
]

# 1️⃣ Dictionary – total spend by each customer
spend_by_customer = {}
for order in orders:
    spend_by_customer[order["customer"]] = order["qty"] * order["price"]

# 2️⃣ Set – unique products sold
unique_products = {order["product"] for order in orders}

# 3️⃣ Tuple – summary (number of orders, total revenue)
total_orders = len(orders)
total_revenue = sum(order["qty"] * order["price"] for order in orders)
summary = (total_orders, total_revenue)

# Display results
print("Spend by Customer:", spend_by_customer)
print("Unique Products:", unique_products)
print("Summary (Orders, Revenue):", summary)

#Explanation 
#List: Stores the 2 orders.
#Dictionary: Calculates how much each customer spent.
#Set: Finds the unique products sold (no repeats).
#Tuple: Keeps a fixed summary — (total orders, total revenue).

#Results
#Roy spent $9.0, Wick spent $6.0.
#2 unique products sold.
#Total revenue = $15.0.

