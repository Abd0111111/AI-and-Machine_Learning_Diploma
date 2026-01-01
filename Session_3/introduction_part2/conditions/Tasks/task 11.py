# =====================================================
# 🧠🔥 FINAL PRACTICE TASK – Python Conditions & Control Flow
# =====================================================
# 📌 This task covers:
# - if
# - if-else
# - if-elif-else
# - match-case (Python 3.10+)
# - break
#
# ❗ Read each requirement carefully.
# ❗ Write clean, readable code.
# ❗ Do NOT use solutions from previous tasks directly.
# =====================================================


# -----------------------------------------------------
# 📝 TASK DESCRIPTION:
# -----------------------------------------------------
# You are building a simple **Console-Based User System**
# that simulates:
# - User login
# - Age verification
# - Grade evaluation
# - Menu navigation
# - Loop control using break
#
# Follow the steps below EXACTLY.
# -----------------------------------------------------


# -----------------------------------------------------
# 1️⃣ USER LOGIN SYSTEM
# -----------------------------------------------------
# 🔹 Create a variable `correct_password` and assign any value.
# 🔹 Create a list called `attempts` containing at least 4 password attempts.
# 🔹 Loop through the attempts:
#     - If the attempt is correct:
#         • Print "Login Successful"
#         • Exit the loop using break
#     - Else:
#         • Print "Wrong Password"


# -----------------------------------------------------
# 2️⃣ AGE VERIFICATION
# -----------------------------------------------------
# 🔹 Create a variable `age`.
# 🔹 Using if-elif-else:
#     - Print "Child" if age < 13
#     - Print "Teenager" if age < 18
#     - Print "Adult" if age < 60
#     - Print "Senior" otherwise


# -----------------------------------------------------
# 3️⃣ GRADE SYSTEM
# -----------------------------------------------------
# 🔹 Create a variable `score`.
# 🔹 Using if-elif-else:
#     - Print "A" if score >= 90
#     - Print "B" if score >= 80
#     - Print "C" if score >= 70
#     - Print "D" if score >= 60
#     - Print "F" otherwise


# -----------------------------------------------------
# 4️⃣ MENU SYSTEM (MATCH-CASE)
# -----------------------------------------------------
# 🔹 Create a variable `choice`.
# 🔹 Use match-case to handle the following:
#     1 -> Print "Create New File"
#     2 -> Print "Open File"
#     3 -> Print "Save File"
#     4 -> Print "Exit Program"
#     _ -> Print "Invalid Choice"
#
# ⚠️ Python 3.10+ required


# -----------------------------------------------------
# 5️⃣ COLOR CLASSIFICATION (MATCH-CASE)
# -----------------------------------------------------
# 🔹 Create a variable `color`.
# 🔹 Use match-case:
#     - Warm colors: red, orange, yellow
#     - Cool colors: blue, green, purple
#     - Neutral colors: black, white, gray
#     - Otherwise print "Unknown Color"


# -----------------------------------------------------
# 6️⃣ SEARCH SYSTEM WITH BREAK
# -----------------------------------------------------
# 🔹 Create a list called `items`.
# 🔹 Create a variable `search_item`.
# 🔹 Loop through the list:
#     - Print each item while searching
#     - If the item is found:
#         • Print "Item Found"
#         • Exit the loop using break


# -----------------------------------------------------
# 🚀 BONUS (OPTIONAL – HARD)
# -----------------------------------------------------
# 🔹 Combine login + menu:
#     - Only show the menu if login is successful
#     - Otherwise stop execution
#
# 💡 Hint:
#     Use a boolean flag like `logged_in = False`
# -----------------------------------------------------


# =====================================================
# ✅ END OF FINAL TASK
# =====================================================

# 1️⃣ USER LOGIN SYSTEM
correct_password = "secure123"
attempts = []

print("Enter 4 password attempts:")
for _ in range(4):
    attempt = input("Password attempt: ")
    attempts.append(attempt)

for attempt in attempts:
    if attempt == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")

# 2️⃣ AGE VERIFICATION
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# 3️⃣ GRADE SYSTEM
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 4️⃣ MENU SYSTEM (MATCH-CASE)
choice = int(input("Menu Choice (1-4): "))

match choice:
    case 1:
        print("Create New File")
    case 2:
        print("Open File")
    case 3:
        print("Save File")
    case 4:
        print("Exit Program")
    case _:
        print("Invalid Choice")

# 5️⃣ COLOR CLASSIFICATION (MATCH-CASE)
color = input("Enter a color: ").lower()

match color:
    case "red" | "orange" | "yellow":
        print("Warm Color")
    case "blue" | "green" | "purple":
        print("Cool Color")
    case "black" | "white" | "gray":
        print("Neutral Color")
    case _:
        print("Unknown Color")

# 6️⃣ SEARCH SYSTEM WITH BREAK
items = ["apple", "banana", "cherry", "date"]
search_item = input("Enter item to search for: ").lower()

for item in items:
    print(item)
    if item == search_item:
        print("Item Found")
        break

# 🚀 BONUS: Login + Menu combined
correct_password = "secure123"
logged_in = False

print("Enter password attempts (max 4):")
for _ in range(4):
    attempt = input("Password attempt: ")
    if attempt == correct_password:
        logged_in = True
        print("Login Successful")
        break
    else:
        print("Wrong Password")

if logged_in:
    choice = int(input("Menu Choice (1-4): "))
    match choice:
        case 1:
            print("Create New File")
        case 2:
            print("Open File")
        case 3:
            print("Save File")
        case 4:
            print("Exit Program")
        case _:
            print("Invalid Choice")
