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

numbers = [1,2,3,4,5,6,7,8,9,10]
list1= pd.Series(numbers)
print(list1)
print(list1[2])