# 📝 Task 5:
# Create a list of prices.
# Use a for loop to calculate and print:
# - Total price
# - Average price

prices = list(map(float, input("Enter prices separated by space: ").split()))
total_price = 0
for price in prices:
    total_price += price
average_price = total_price / len(prices) if prices else 0
print("Total price:", total_price)
print("Average price:", average_price)