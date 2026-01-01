# HARD TASK 2: E-Commerce Order Processor
# ============================================================
# Task Description:
# Create a function that processes an order with:
# - Customer name as positional argument
# - Any number of ordered item prices using *args
# - Default discount rate (default = 0%)
# - Extra order details using **kwargs
#
# The function should:
# - Calculate total price
# - Apply discount
# - Print a detailed order summary
# ============================================================

def process_order(customer_name, *prices, discount=0, **order_info):
    print("Order Summary")
    print("-------------")
    print(f"Customer: {customer_name}")

    total = sum(prices)
    discount_amount = total * (discount / 100)
    final_price = total - discount_amount

    print(f"Items Prices: {prices}")
    print(f"Subtotal: ${total}")
    print(f"Discount: {discount}%")
    print(f"Final Price: ${final_price}")

    if order_info:
        print("Order Details:")
        for key, value in order_info.items():
            print(f"- {key}: {value}")


# Model Answer Execution
process_order(
    "Alice",
    100, 250, 150,
    discount=10,
    payment_method="Credit Card",
    delivery="Express"
)