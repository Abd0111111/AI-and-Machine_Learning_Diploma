# 📝 Task 5:
# Create a variable score.
# Print:
# "A" if score >= 90
# "B" if score >= 80
# "C" if score >= 70
# "Fail" otherwise

score = int(input("Enter score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")