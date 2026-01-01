# Task 7:
# Display general information about the dataset using info().
# --------------------------------------------
import pandas as pd

data = pd.read_csv("E:\AI& Machine Learning Diploma Folder\PythonProject\Session_10\pandas_Libaliry\data.csv")
print(data.head())
data.info()
