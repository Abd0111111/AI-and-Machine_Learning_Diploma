# --------------------------------------------
# Task 3:
# Create a DataFrame from a dictionary with Calories and Time columns.
# --------------------------------------------
import pandas as pd
data = {
    "Calories": [200, 350, 400, 150],
    "Time": [30, 45, 50, 20]
}
df = pd.DataFrame(data)
print(df)