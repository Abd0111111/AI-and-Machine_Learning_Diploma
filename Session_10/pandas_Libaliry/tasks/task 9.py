# --------------------------------------------
# Task 9:
# Create a new column called CalorieLevel:
# - High if Calories > 400
# - Normal otherwise
# --------------------------------------------
import pandas as pd
data9 = pd.read_csv("../data.csv")
data9['CalorieLevel']=data9['Calories'].apply(lambda x : 'high' if x > 400 else 'normal')
print(data9['CalorieLevel'].tail(10))