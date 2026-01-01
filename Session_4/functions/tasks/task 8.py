# TASK DESCRIPTION:
# Create a function called `process_order` that simulates an
# online shopping system.
#
# Requirements:
# 1. The function must accept:
#    - A positional argument `customer_name`
#    - Variable-length positional arguments (*items)
#    - A default argument `tax_rate` with a default value of 0.14
#    - Variable-length keyword arguments (**details)
#
# 2. Each item in *items is a tuple in the form:
#    (item_name, price, quantity)
#
# 3. The function should:
#    - Print customer name
#    - Print all items with their total price
#    - Calculate subtotal
#    - Calculate tax
#    - Calculate final total
#    - Print any extra details passed via **details
#
# 4. If no items are provided, print a warning message.
#
# ------------------------------------------------------------
# SOLUTION:
# ------------------------------------------------------------

def process_order(customer_name, *items, tax_rate=0.14, **details):
    print("🧾 Order Summary")
    print("-" * 40)
    print(f"Customer: {customer_name}")

    # 🛑 If no items were provided
    if not items:
        print("⚠️ No items in the order.")
        return

    subtotal = 0

    print("\n📦 Items:")
    for item in items:
        item_name, price, quantity = item
        item_total = price * quantity
        subtotal += item_total
        print(f"- {item_name}: {price} x {quantity} = {item_total}")

    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    print("\n💰 Payment Details:")
    print(f"Subtotal: {subtotal}")
    print(f"Tax ({tax_rate * 100}%): {tax_amount}")
    print(f"Total: {total}")

    # 📌 Extra details using **kwargs
    if details:
        print("\n📌 Additional Details:")
        for key, value in details.items():
            print(f"{key}: {value}")

    print("-" * 40)
    print("✅ Order processed successfully!\n")


# ------------------------------------------------------------
# FUNCTION CALLS (TEST CASES)
# ------------------------------------------------------------

process_order(
    "Omar",
    ("Laptop", 15000, 1),
    ("Mouse", 300, 2),
    ("Keyboard", 700, 1),
    tax_rate=0.10,
    payment_method="Credit Card",
    delivery="Express"
)

process_order(
    "Ahmed",
    ("Phone", 8000, 1),
    ("Headphones", 1200, 1)
)

process_order("Sara")  # No items case
