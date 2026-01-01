# 📝 Task 6:
# Create a list of names.
# Use enumerate() to print:
# index -> name
# Example: 0 -> Ahmed

names = input("Enter names separated by space: ").split()
for idx, name in enumerate(names):
    print(f"{idx} -> {name}")
