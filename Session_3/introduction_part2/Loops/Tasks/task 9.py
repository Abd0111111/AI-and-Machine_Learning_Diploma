# 📝 Task 9:
# Create a list of numbers.
# Search for a specific number.
# If found, print "Number Found" and stop the loop.
# If NOT found, print "Number Not Found" using for-else.

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
search_num = int(input("Enter number to search for: "))
for num in numbers:
    if num == search_num:
        print("Number Found")
        break
else:
    print("Number Not Found")
