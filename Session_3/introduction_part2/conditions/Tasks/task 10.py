# 📝 Task 10:
# Create a list of names.
# Search for a specific name.
# When found, print "Name Found" and stop the loop using break.

names = []
n = int(input("Enter number of names: "))
for _ in range(n):
    names.append(input("Enter name: "))

search_name = input("Enter name to search for: ")
for name in names:
    if name == search_name:
        print("Name Found")
        break