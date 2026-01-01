# 📝 Task 14:
# Build a mini system:
# - Create a list of commands (e.g. start, run, pause, stop)
# - Loop through commands using while
# - Print each command
# - Stop the loop when command == "stop"
# - If loop finishes without stop, print "No stop command found"

commands = input("Enter commands separated by space: ").split()  # Get commands list from user input

index = 0  # Initialize index for loop control
while index < len(commands):  # Loop over commands while index is within list range
    cmd = commands[index]  # Get current command at index
    print(cmd)  # Print the current command
    if cmd == "stop":  # Check if the command is "stop"
        break  # Exit the loop immediately if stop found
    index += 1  # Move to next command index
else:
    # Executes only if while loop completes without encountering 'break'
    print("No stop command found")
