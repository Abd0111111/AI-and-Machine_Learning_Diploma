# ============================================
# Pandas Basics - Practice Tasks (Instructor Version)
# Each task includes:
# - Task written as a question (comment)
# - Directly followed by the solution code
# ============================================

import pandas as pd

# --------------------------------------------
# Task 1:
# Create a list of numbers, convert it to a pandas Series,
# then print the full Series and the element at index 2.
# --------------------------------------------

numbers = [10, 20, 30, 40, 50]
series_numbers = pd.Series(numbers)
print(series_numbers)
print(series_numbers[2])