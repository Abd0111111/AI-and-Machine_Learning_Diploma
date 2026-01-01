# 📝 Task 7:
# Use nested for loops to print a 5x5 grid of stars (*).
# Example:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for _ in range(5):
    for _ in range(5):
        print("*", end=" ")
    print()