# 📝 Task 2:
# Create a string.
# Use a for loop to count how many vowels (a, e, i, o, u) are in the string.
# Print the final count.

string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for ch in string:
    if ch in vowels:
        count += 1
print(count)