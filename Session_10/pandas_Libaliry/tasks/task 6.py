# Task 6:
# Read the CSV file (data.csv) and print:
# - The first 5 rows
# - The last 10 rows
# --------------------------------------------
import pandas as pd
import os
if os.path.exists("data.csv"):
    data_csv = pd.read_csv("data.csv")
    print(data_csv.head())
    print(data_csv.tail(10))
else:
    print("data.csv file not found")
