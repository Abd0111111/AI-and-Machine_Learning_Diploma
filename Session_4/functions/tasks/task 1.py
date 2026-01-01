# Task 1: Positional Arguments
# ------------------------------------------------------------
# Task Description:
# Create a function that receives three positional arguments:
# (product_name, price, quantity)
# The function should calculate the total cost and print
# a formatted invoice message.
# ------------------------------------------------------------

def calculate_total(product_name, price, quantity):
    total = price * quantity
    print(f"Product: {product_name}")
    print(f"Price: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total Cost: ${total}")


# Model Answer Execution
calculate_total("Laptop", 1200, 2)