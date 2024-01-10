import os
import pandas as pd

##################################################

# TASK 1

##################################################

# Default file name will be data.csv if it exists, otherwise data_example.csv
script_directory = os.path.dirname(__file__)
file_name = "data.csv"
file_path = os.path.join(script_directory, file_name)

if not(os.path.exists(file_path)):
    file_name = "data_example.csv"

file_path = os.path.join(script_directory, file_name)

# Read the csv file into a pandas dataframe
df = pd.read_csv(file_path)
print(f"Collected {df.shape[0]} records from {file_name}")

# Remove records with potential errors
df = df.dropna()
df = df[df['Age'] >= 0]
print(f"Collected {df.shape[0]} records after removing invalid records from {file_name}")

# Calculate the average age
average_age = df['Age'].mean()
print(f"Average age is of individuals: {average_age:.2f}")