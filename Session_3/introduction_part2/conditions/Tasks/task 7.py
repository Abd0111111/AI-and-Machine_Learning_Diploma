# 📝 Task 7:
# Create a variable day.
# Use match-case to print:
# "Weekend" for Saturday or Sunday
# "Weekday" otherwise
day = input("Enter day: ")
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")