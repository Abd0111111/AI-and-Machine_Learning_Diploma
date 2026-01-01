# --------------------------------------------
# Task 2:
# Create a pandas Series with custom index names (day1, day2, day3, day4)
# that stores temperatures. Print the value of day3.
# --------------------------------------------
import pandas as pd
temps = [22, 25, 23, 26]
temp_series = pd.Series(temps, index=["day1", "day2", "day3", "day4"])
print(temp_series)
print(temp_series["day3"])