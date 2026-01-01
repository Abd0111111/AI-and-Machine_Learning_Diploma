# 📝 Task 11:
# Use a while loop to reverse a string WITHOUT using slicing or reversed().

string = input("Enter string to reverse: ")
reversed_str = ""
index = len(string) - 1
while index >= 0:
    reversed_str += string[index]
    index -= 1
print(reversed_str)