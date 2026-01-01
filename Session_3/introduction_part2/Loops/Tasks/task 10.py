# 📝 Task 10:
# Use a while loop to print numbers from 1 to 100.
# Print ONLY numbers divisible by both 3 and 5.


i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1

# Task 11
string = input("Enter string to reverse: ")
reversed_str = ""
index = len(string) - 1
while index >= 0:
    reversed_str += string[index]
    index -= 1
print(reversed_str)