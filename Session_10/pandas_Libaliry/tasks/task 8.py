# --------------------------------------------
# Task 8:
# Display statistical summary using describe()
# then print the mean and max of the Calories column.
# --------------------------------------------
import pandas as pd
import os
if os.path.exists("E:\AI& Machine Learning Diploma Folder\PythonProject\Session_10\pandas_Libaliry\data.csv"):
    stats = data_csv.describe()
    print(stats)
    print("Calories Mean:", stats.loc["mean", "Calories"])
    print("Calories Max:", stats.loc["max", "Calories"])
