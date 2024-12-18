import pandas as pd
import re

# Load the CSV file
file_path = 'carmarketnepal_with_model_name.csv' 
data = pd.read_csv(file_path)

# Function to clean text: remove dirty letters, symbols, and decimal numbers
def clean_text(text):
    # Removing dirty characters like â€˜Sâ€™ and any other non-alphanumeric characters except spaces
    text = re.sub(r"[^\w\s]", "", text)
    # Removing any decimal numbers
    text = re.sub(r"\d+\.\d+", "", text)
    return text.strip()

# Function to extract the first two words and clean the result
def extract_first_two_words_cleaned(text):
    # Splitting the string into words
    words = text.split()
    # Extracting first two words (if available) and join them
    clean_words = " ".join(words[:2]) if len(words) >= 2 else words[0] if len(words) == 1 else ""
    # Cleaning the extracted text
    return clean_text(clean_words)

# Applying the function to the 'specific_model' column and create a new column 'model_name'
data['model_name'] = data['specific_model'].astype(str).apply(extract_first_two_words_cleaned)

# Saving the updated DataFrame to a new CSV file
output_file_path = 'carmarketnepal_with_clean_model_name.csv'
data.to_csv(output_file_path, index=False)

print(f"Updated CSV file saved as: {output_file_path}")
