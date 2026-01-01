# HARD TASK 1: User Management System
# ============================================================
# Task Description:
# Create a function that:
# - Takes a required positional argument: username
# - Accepts multiple hobbies using *args
# - Has a default argument for role (default = "User")
# - Accepts additional user details using **kwargs
#
# The function should print a complete user profile.
# ============================================================

def create_user_profile(username, *hobbies, role="User", **details):
    print("User Profile")
    print("------------")
    print(f"Username: {username}")
    print(f"Role: {role}")

    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")
    else:
        print("Hobbies: None")

    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"- {key}: {value}")
    else:
        print("Additional Details: None")


# Model Answer Execution
create_user_profile(
    "omar_gaber",
    "Coding",
    "Reading",
    role="Admin",
    age=22,
    country="Egypt"
)