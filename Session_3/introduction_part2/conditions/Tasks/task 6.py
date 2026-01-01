# 📝 Task 6:
# Create a variable age.
# Print:
# "Child" if age < 13
# "Teen" if age < 18
# "Adult" otherwise
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")