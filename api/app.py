from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel, Field
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
import os
import uvicorn
# Initialize FastAPI app
app = FastAPI(
    title="Football Player Value Prediction API",
    description="🚀 Predict the estimated transfer value (€) of a football player based on their attributes.",
    version="1.0"
)

app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    with open(Path(__file__).parent / "static" / "index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)



# Load the trained model, scaler, and label encoders
model = joblib.load("models/football_value_predictor.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")

# Define the request body with Swagger descriptions
class PlayerData(BaseModel):
    Overall: int = Field(..., example=85, description="Overall skill rating of the player.")
    Finishing: int = Field(..., example=80, description="Player's finishing ability (0-100).")
    Wage: float = Field(..., example=200000.0, description="Player's weekly wage in Euros (€).")
    Potential: int = Field(..., example=90, description="Potential maximum rating of the player.")
    Reactions: int = Field(..., example=85, description="Player's reaction speed (0-100).")
    Weight: float = Field(..., example=74.8, description="Weight in kilograms (kg).")
    Age: int = Field(..., example=25, description="Age of the player in years.")
    BallControl: int = Field(..., example=85, description="Player's ball control skill (0-100).")
    Dribbling: int = Field(..., example=88, description="Player's dribbling skill (0-100).")
    Stamina: int = Field(..., example=78, description="Player's stamina level (0-100).")
    Vision: int = Field(..., example=82, description="Player's vision attribute (0-100).")
    PreferredFoot: int = Field(..., example=1, description="Encoded Preferred Foot (0=Left, 1=Right).")
    Height: float = Field(..., example=175.3, description="Height in centimeters (cm).")

# Function to preprocess input data
def preprocess_data(data: PlayerData):
    # Creating the DataFrame with the correct feature order
    df = pd.DataFrame([[  
        data.Overall, data.Finishing, data.Wage, data.Potential, data.Reactions, data.Weight,
        data.Age, data.BallControl, data.Dribbling, data.Stamina, data.Vision,
        data.PreferredFoot, data.Height
    ]], columns=["Overall", "Finishing", "Wage", "Potential", "Reactions", "Weight", 
                "Age", "BallControl", "Dribbling", "Stamina", "Vision", 
                 "PreferredFoot", "Height"])

    # Print the columns to verify order
    print("Input DataFrame columns:", df.columns)  # Verify columns during prediction

    # Scale numerical data using the saved scaler
    df_scaled = scaler.transform(df)
    return df_scaled

# Prediction Endpoint
@app.post("/predict", summary="⚽ Predict Football Player Value")
def predict_player_value(player_data: PlayerData):
    """
    📌 **Predicts the estimated market value of a football player.**
    """
    try:
        processed_data = preprocess_data(player_data)
        prediction = model.predict(processed_data)
        return {"Predicted Value (€)": round(prediction[0], 2)}
    except Exception as e:
        return {"error": str(e)}

# Root Endpoint
@app.get("/", summary="🏠 API Home")
def home():
    return {"message": "Football Player Value Prediction API is running!"}

# Run the API server
if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)  # Dynamically use the port
    uvicorn.run(app, host="127.0.0.1", port=int(port))

