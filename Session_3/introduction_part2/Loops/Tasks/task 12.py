
# 📝 Task 12:
# Create a while True loop that keeps asking for a number (simulate using a list).
# Stop the loop when the number entered is 0.
# Print each number before stopping.

numbers = list(map(int, input("Enter numbers separated by space (0 to stop): ").split()))
idx = 0
while True:
    if idx >= len(numbers):
        break
    num = numbers[idx]
    print(num)
    if num == 0:
        break
    idx += 1