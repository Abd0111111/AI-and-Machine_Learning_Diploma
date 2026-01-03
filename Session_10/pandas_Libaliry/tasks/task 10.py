# --------------------------------------------
# Task 10:
# Handle missing values by replacing missing Calories
# with the mean value of the column.
# --------------------------------------------
import pandas as pd
data10 = pd.read_csv("../data.csv")
data_10 = data10.dropna()
print(data_10)