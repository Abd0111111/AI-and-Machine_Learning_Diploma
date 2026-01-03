# Task 6:
# Read the CSV file (data.csv) and print:
# - The first 5 rows
# - The last 10 rows
# --------------------------------------------
import pandas as pd
data4 = pd.read_csv('../data.csv')
print(data4.head())
print(data4.tail(10))