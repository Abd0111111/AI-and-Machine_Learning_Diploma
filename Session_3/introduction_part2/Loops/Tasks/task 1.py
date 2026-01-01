# 📝 Task 1:
# Create a list of at least 5 numbers.
# Use a for loop to print ONLY the numbers greater than 10.

numbers = list(map(int, input("Enter at least 5 numbers separated by space: ").split()))
for num in numbers:
    if num > 10:
        print(num)