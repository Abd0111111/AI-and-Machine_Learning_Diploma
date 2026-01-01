# 📝 Task 13:
# Create a list of integers.
# Search for a negative number using while.
# If found, print "Negative Found" and stop.
# If not found, print "All numbers are positive" using while-else.

nums = list(map(int, input("Enter integers separated by space: ").split()))
index = 0
while index < len(nums):
    if nums[index] < 0:
        print("Negative Found")
        break
    index += 1
else:
    print("All numbers are positive")