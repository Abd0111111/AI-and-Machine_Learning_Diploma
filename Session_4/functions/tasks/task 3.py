# Task 3: Default Arguments
# ------------------------------------------------------------
# Task Description:
# Create a function that greets a user.
# The greeting message should be optional and default to "Hello".
# ------------------------------------------------------------

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# Model Answer Execution
greet_user("Alice")
greet_user("Bob", "Welcome")
