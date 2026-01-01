# 📝 Task 8:
# Create a variable choice.
# Use match-case:
# 1 -> "Play Game"
# 2 -> "Settings"
# 3 -> "Exit"
# Default -> "Invalid Choice"

choice = int(input("Enter choice (1-3): "))
match choice:
    case 1:
        print("Play Game")
    case 2:
        print("Settings")
    case 3:
        print("Exit")
    case _:
        print("Invalid Choice")
