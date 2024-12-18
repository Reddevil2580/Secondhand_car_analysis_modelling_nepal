import pandas as pd

# Loading the CSV file
file_path = 'carmarketnepal_data_with_specific_model_cleaned.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Function to extract the first two words from a string
def extract_first_two_words(text):
    words = text.split()  # Split the string into words
    if len(words) >= 2:   # If two or more words exist, extract the first two
        return " ".join(words[:2])
    elif len(words) == 1:  # If only one word exists, return it
        return words[0]
    return ""  # If the text is empty or invalid, return an empty string

# Applying the function to the 'specific_model' column and create a new column 'model_name'
data['model_name'] = data['specific_model'].astype(str).apply(extract_first_two_words)

# Save the updated DataFrame to a new CSV file
output_file_path = 'carmarketnepal_with_model_name.csv'
data.to_csv(output_file_path, index=False)

print(f"Updated CSV file saved as: {output_file_path}")
