# --------------------------------------------
# Task 8:
# Display statistical summary using describe()
# then print the mean and max of the Calories column.
# --------------------------------------------
import pandas as pd

stats = pd.read_csv("../data.csv")
summary = stats.describe()
print(summary)

print("Calories Mean:", stats["Calories"].mean())
print("Calories Max:", stats["Calories"].max())