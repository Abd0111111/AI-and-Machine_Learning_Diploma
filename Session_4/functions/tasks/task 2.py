# Task 2: Keyword Arguments
# ------------------------------------------------------------
# Task Description:
# Create a function that displays user profile information.
# The function should accept keyword arguments so the order
# of arguments does not matter.
# ------------------------------------------------------------

def display_profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


# Model Answer Execution
display_profile(age=25, city="Cairo", name="Omar")