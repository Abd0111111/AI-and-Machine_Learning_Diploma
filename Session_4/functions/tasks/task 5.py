# Task 5: Variable-length Keyword Arguments (**kwargs)
# ------------------------------------------------------------
# Task Description:
# Create a function that prints configuration settings.
# The function should accept any number of keyword arguments.
# ------------------------------------------------------------

def show_settings(**settings):
    print("Application Settings:")
    for key, value in settings.items():
        print(f"- {key}: {value}")


# Model Answer Execution
show_settings(theme="dark", language="English", version="1.0")
