# ============================================================
# HARD COMPREHENSIVE TASK - PANDAS
# Instructor Model Solution (Doctor Version)
# ❌ os module is NOT used
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# Task 1:
# Load the CSV file into a DataFrame
# ------------------------------------------------------------
df = pd.read_csv("../data.csv")
print("Original DataFrame:")
print(df)

print("\n" + "="*60 + "\n") #ده بس علشان يعمل سطر فاصل

# ------------------------------------------------------------
# Task 2:
# Display general information about the dataset
# (Columns, non-null counts, data types, memory usage)
# ------------------------------------------------------------
print("Dataset Info:")
df.info()

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 3:
# Display statistical summary of numerical columns
# ------------------------------------------------------------
print("Statistical Description:")
print(df.describe())

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 4:
# Handle missing values in 'Calories' column
# Replace NaN values with the mean
# ------------------------------------------------------------
mean_calories = df["Calories"].mean()
print(f"Mean Calories: {mean_calories}")

df["Calories"].fillna(mean_calories, inplace=True)

print("\nAfter Filling Missing Values:")
print(df)

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 5:
# Create a new column 'Calorie_Level'
# High if Calories > 400, otherwise Normal
# ------------------------------------------------------------
df["Calorie_Level"] = df["Calories"].apply(
    lambda x: "High" if x > 400 else "Normal"
)

print("After Adding Calorie_Level Column:")
print(df)

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 6:
# Filter rows where Calories are greater than 450
# ------------------------------------------------------------
high_calories_df = df[df["Calories"] > 450]

print("Rows with Calories > 450:")
print(high_calories_df)

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 7:
# Use loc to select specific rows and columns
# Select rows from index 0 to 3 and columns Calories & Duration
# ------------------------------------------------------------
selected_data = df.loc[0:3, ["Calories", "Duration"]]

print("Selected Rows and Columns using loc:")
print(selected_data)

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 8:
# Perform manual statistical calculations
# ------------------------------------------------------------
print("Manual Statistics:")
print("Maximum Calories:", df["Calories"].max())
print("Minimum Calories:", df["Calories"].min())
print("Average Calories:", df["Calories"].mean())

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 9:
# Count how many High vs Normal calorie levels
# ------------------------------------------------------------
print("Calorie Level Counts:")
print(df["Calorie_Level"].value_counts())

print("\n" + "="*60 + "\n")

# ------------------------------------------------------------
# Task 10:
# Display final cleaned DataFrame
# ------------------------------------------------------------
print("Final Cleaned DataFrame:")
print(df)

# ============================================================
# END OF HARD TASK
# ============================================================
