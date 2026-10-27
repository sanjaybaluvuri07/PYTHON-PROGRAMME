
# Integrated E-Commerce Order Processing and Reconciliation

inventory = {
    "Laptop": 10,
    "Phone": 20,
    "Headphones": 15
}

prices = {
    "Laptop": 50000,
    "Phone": 15000,
    "Headphones": 2000
}

orders = [
    {"product": "Laptop", "quantity": 2, "discount": 10,
     "dispatched": 2, "returned": 0},
    {"product": "Phone", "quantity": 3, "discount": 5,
     "dispatched": 2, "returned": 1},
    {"product": "Headphones", "quantity": 4, "discount": 0,
     "dispatched": 4, "returned": 1}
]

total_revenue = 0

print("E-COMMERCE ORDER PROCESSING")
print("-" * 45)

for order in orders:
    product = order["product"]
    quantity = order["quantity"]
    discount = order["discount"]
    dispatched = order["dispatched"]
    returned = order["returned"]

    print(f"\nProduct: {product}")

    # Validate order and dispatch quantities
    if (quantity <= 0 or dispatched < 0 or
            dispatched > quantity or returned < 0 or
            returned > dispatched or
            discount < 0 or discount > 100):
        print("Error: Invalid order details")
        continue

    if quantity > inventory[product]:
        print("Error: Insufficient stock")
        continue

    # Calculate discounted price
    unit_price = prices[product]
    discounted_price = unit_price * (1 - discount / 100)

    # Calculate revenue for items retained by customers
    sold_quantity = dispatched - returned
    revenue = sold_quantity * discounted_price
    total_revenue += revenue

    # Update inventory: dispatch stock, then add returns
    inventory[product] -= dispatched
    inventory[product] += returned

    # Identify unfulfilled orders
    pending = quantity - dispatched

    print("Ordered:", quantity)
    print("Dispatched:", dispatched)
    print("Returned:", returned)
    print("Pending:", pending)
    print("Discount:", discount, "%")
    print("Revenue:", f"Rs. {revenue:.2f}")

    if pending > 0:
        print("Discrepancy: Order not fully dispatched")
    elif returned > 0:
        print("Discrepancy: Product return recorded")
    else:
        print("Status: Order completed")

# Final reconciliation
print("\nFINAL RECONCILIATION")
print("-" * 45)
print("Total Revenue: Rs.", f"{total_revenue:.2f}")

print("\nFINAL INVENTORY SUMMARY")
for product, stock in inventory.items():
    print(product, ":", stock, "units remaining")
