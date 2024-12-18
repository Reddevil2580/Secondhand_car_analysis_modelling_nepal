import pandas as pd
import re

# Load the CSV file into a DataFrame
df = pd.read_csv('carmarketnepal_data.csv')

# Defining the regex pattern to capture a 4-digit number
pattern = r'\b(\d{4})\b'

# Extracting the year from the 'Model' column and store it in a new 'Year' column
df['Year'] = df['Model'].str.extract(pattern)

# Filling any NaN values (if year not found) with 0 and convert to integer
df['Year'] = df['Year'].fillna(0).astype(int)

# Saving the updated DataFrame, including the Year column, to a new CSV file
df.to_csv('carmarketnepal_data_with_year.csv', index=False)

print("Data saved to 'carmarketnepal_data_with_year.csv' successfully.")
