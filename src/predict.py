import joblib
import pandas as pd

# Load trained model
model = joblib.dump(rf_model, "models/football_value_predictor.pkl")
joblib.dump(scaler, "models/scaler.pkl")

# Example new player
new_player = pd.DataFrame([{
  "Overall": 15,
  "Finishing": 80,
  "Wage": 200000,
  "Potential": 90,
  "Reactions": 85,
  "Weight": 74.8,
  "Age": 95,
  "BallControl": 85,
  "Dribbling": 88,
  "Stamina": 78,
  "Vision": 82,
  "PreferredFoot": 1,
  "Height": 175.3
}])

# Ensure new player has the same columns as training data
X_train = pd.read_csv("data/processed_data.csv").drop(columns=["Value"])
new_player = new_player[X_train.columns]

# Predict market value
predicted_value = model.predict(new_player)[0]
print(f"Predicted Market Value: €{predicted_value:,.2f}")
