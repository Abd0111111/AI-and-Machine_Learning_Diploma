# Python Control Flow Tasks 🧠🐍
# ---------------------------------------------------------
# 1. If Statement Tasks

# Task 1️⃣

# 📝 Task:
# Check if a person is eligible to vote.
# If age is 18 or more, print "Eligible to vote"

age = 20

if age >= 18:
    print("Eligible to vote")

# Task 2️⃣
# 📝 Task:
# Check if the temperature is hot.
# If temperature is greater than 30, print "Hot Weather"

temperature = 35

if temperature > 30:
    print("Hot Weather")
# ---------------------------------------------------------
# 2. If-Else Statement Tasks

# Task 3️⃣

# 📝 Task:
# Check if a number is even or odd using if-else
number = 9

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 4️⃣
# 📝 Task:
# Check login status.
# If password is correct print "Login Success"
# Otherwise print "Wrong Password"

password = "admin"

if password == "admin":
    print("Login Success")
else:
    print("Wrong Password")

# ---------------------------------------------------------
# 3. If-Elif-Else Tasks

# Task 5️⃣
# 📝 Task:
# Determine grade based on score

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

# Task 6️⃣
# 📝 Task:
# Categorize age group

age = 12

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
# ---------------------------------------------------------
# 4. Match Case Tasks (Python 3.10+)
# Task 7️⃣
# 📝 Task:
# Print day type based on day name

day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")

# Task 8️⃣
# 📝 Task:
# Menu selection using match-case

choice = 3

match choice:
    case 1:
        print("Play Game")
    case 2:
        print("Settings")
    case 3:
        print("Exit")
    case _:
        print("Invalid Choice")
# ---------------------------------------------------------
# 5. Break Statement Tasks
# Task 9️⃣
# 📝 Task:
# Stop loop when number reaches 4

for i in range(1, 10):
    print(i)
    if i == 4:
        break

# Task 🔟

# 📝 Task:
# Search for a name in a list and stop when found

names = ["Ali", "Omar", "Sara", "Mona"]
search = "Sara"

for name in names:
    print(name)
    if name == search:
        print("Name Found")
        break