# --------------------------------------------
# Bonus Task (Medium Level):
# Perform the following steps:
# 1- Read the CSV file
# 2- Fill missing Calories with the mean
# 3- Create CalorieLevel column
# 4- Display info(), describe(), and all High calorie rows
# --------------------------------------------

import pandas as pd
data11 = pd.read_csv("../data.csv")
main = data11['Calories'].main()
data11.fillna(main, inplace = True)
print(data11)