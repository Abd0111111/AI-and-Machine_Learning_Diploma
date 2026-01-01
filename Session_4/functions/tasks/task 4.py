# Task 4: Variable-length Positional Arguments (*args)
# ------------------------------------------------------------
# Task Description:
# Create a function that accepts any number of numbers
# and returns their average.
# ------------------------------------------------------------

def calculate_average(*numbers):
    if len(numbers) == 0:
        print("No numbers provided")
        return

    average = sum(numbers) / len(numbers)
    print(f"Numbers: {numbers}")
    print(f"Average: {average}")


# Model Answer Execution
calculate_average(10, 20, 30)
calculate_average(5, 15)

