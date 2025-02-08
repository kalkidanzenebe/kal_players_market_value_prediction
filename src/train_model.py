import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the processed dataset
df = pd.read_csv("data/processed_data.csv")

# Split features (X) and target (y)
X = df.drop(columns=['Value'])  # Drop the target column 'Value'
y = df['Value']  # Target variable 'Value'

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize scaler and apply it
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize RandomForest model
rf_model = RandomForestRegressor(n_estimators=200, max_depth=30, random_state=42)
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print metrics
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-Squared: {r2}")

# Save the trained model, scaler, and label encoders
joblib.dump(rf_model, "models/football_value_predictor.pkl")
joblib.dump(scaler, "models/scaler.pkl")

# Save the label encoders used during preprocessing (ensure these match the ones used during training)
import joblib
joblib.dump(LabelEncoder, "models/label_encoders.pkl")

print("Model training complete and saved.")
