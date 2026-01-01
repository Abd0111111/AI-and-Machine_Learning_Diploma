# Task 4:
# Using .loc:
# 1- Print the row with index 1
# 2- Print rows with index 1 and 2
# 3- Print rows from index 1 to 3
# --------------------------------------------
import pandas as pd


data = {
    "Calories": [200, 350, 400, 150],
    "Time": [30, 45, 50, 20]
}


df = pd.DataFrame(data)


print(df)
print(df.loc[1])
print(df.loc[[1, 2]])
print(df.loc[1:3])