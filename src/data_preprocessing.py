import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/sample_4000.csv")

# Rename 'Preferred Foot' to 'PreferredFoot' to match model
df.rename(columns={'Preferred Foot': 'PreferredFoot'}, inplace=True)

# Handle categorical columns with label encoding
categorical_cols = df.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Convert Height from "5'9"" to total inches
df["Height"] = df["Height"].apply(lambda x: int(x.split("'")[0]) * 12 + int(x.split("'")[1]) if isinstance(x, str) else x)

# Convert Weight from "165lbs" to integer
df["Weight"] = df["Weight"].apply(lambda x: int(x.replace("lbs", "")) if isinstance(x, str) else x)

# Function to convert currency
def convert_currency(value):
    if isinstance(value, str):
        value = value.replace("€", "").replace("K", "000").replace("M", "000000")
        return float(value)
    return value

# Apply function to 'Value' and 'Wage' columns
df["Value"] = df["Value"].apply(convert_currency)
df["Wage"] = df["Wage"].apply(convert_currency)

# Save the processed data
df.to_csv("data/processed_data.csv", index=False)

# Optionally, save the label encoders to be used later during prediction
import joblib
joblib.dump(label_encoders, "models/label_encoders.pkl")
