import pandas as pd
import re

df = pd.read_csv('carmarketnepal_data.csv')

# Converting all values in the Model column to strings to avoid TypeError
df['Model'] = df['Model'].astype(str)

brands = ['Hyundai', 'Toyota', 'Kia', 'Honda', 'Ford', 'Suzuki', 'Nissan', 'Mitsubishi', 'Volkswagen', 'Chevrolet', 'Renault', 'Skoda', 'Mahindra', 'Tata', 'Maruti']
extra_words = ['Model', 'Fully', 'Loaded', 'Like', 'Brand', 'New', 'AUTOMATIC', 'with', 'SUNROOF', '4X4', 'Edition', 'Variant']

def extract_specific_model(model_str):
    # Handling cases where model_str might be 'nan'
    if model_str.lower() == 'nan':
        return ""

    # Removing 4-digit years
    model_str = re.sub(r'\b\d{4}\b', '', model_str)
    
    # Split into words
    words = model_str.split()
    
    # Remove brand names
    cleaned_words = [w for w in words if w.capitalize() not in brands]
    
    # Remove extraneous words
    extra_lower = [w.lower() for w in extra_words]
    cleaned_words = [w for w in cleaned_words if w.lower() not in extra_lower]
    
    # Join the remaining words
    specific_model = " ".join(cleaned_words).strip()
    return specific_model

df['specific_model'] = df['Model'].apply(extract_specific_model)

print(df[['Model', 'specific_model']].head())
df.to_csv('carmarketnepal_data_with_specific_model.csv', index=False)
