# Task 5:
# Create a DataFrame with Name, Age, and City.
# Print only the rows where Age is greater than 30.
# --------------------------------------------
import pandas as pd

people = {
    "Name": ["Ahmed", "Mohamed", "Hossam", "Heba", "Mostafa"],
    "Age": [25, 30, 35, 40, 28],
    "City": ["Cairo", "Alex", "Giza", "Luxor", "Aswan"]
}

df_people = pd.DataFrame(people)
print(df_people[df_people["Age"] > 30])

