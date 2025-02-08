# Player Market Value Prediction

## Project Overview

This project is developed as part of the **Fundamentals of Machine Learning** course. The goal is to predict the market value of football players using machine learning techniques. The dataset used consists of player attributes from FIFA17, and the model is built using regression techniques to estimate a player's market value.

## Dataset

- **Source**: [FIFA17 dataset](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database)
- **Rows**: 17,560
- **Columns**: 59
- **Structure**: The dataset includes various player attributes such as Age, Nationality, Overall Rating, Potential, Position, Club, Wage, Skill Moves, and many more.

### Data Documentation

- **Source of Data**: The dataset was obtained from Kaggle.
- **License / Terms of Use**: The dataset is publicly available on Kaggle; check the dataset page for specific licensing terms.
- **Data Structure**: The dataset is organized in a structured CSV format with 59 columns representing different player attributes.
- **Features**: The dataset includes key features such as:
  - **Personal Information**: ID, Name, Age, Nationality
  - **Performance Metrics**: Overall Rating, Potential, Skill Moves, Weak Foot
  - **Financial Information**: Value, Wage
  - **Club Information**: Club Name, Contract Valid Until, Loaned From
  - **Physical Attributes**: Height, Weight, Preferred Foot
  - **Technical Skills**: Passing, Dribbling, Shooting, Defending, Goalkeeping Attributes
- **Source**: FIFA17 dataset
- **Rows**: 17,560
- **Columns**: 59
- **Structure**: The dataset includes various player attributes such as Age, Nationality, Overall Rating, Potential, Position, Club, Wage, Skill Moves, and many more.

## Problem Definition

The objective of this project is to develop a predictive model that estimates the market value of football players based on their attributes. Accurately predicting a player's market value is crucial for clubs, scouts, and analysts to make informed decisions regarding player transfers and contracts. The challenge arises due to the dynamic nature of player valuation, which is influenced by multiple factors such as performance, potential, club reputation, and market trends. The problem is formulated as a regression task, where the target variable is the player's market value.

## Data Preprocessing

- Converted player height and weight into numeric values (cm and kg respectively).
- Handled missing values and outliers.
- Encoded categorical features (e.g., Club, Nationality, Position).
- Scaled numerical features for better model performance.

## Exploratory Data Analysis (EDA)

- Visualized distributions of key features.
- Examined correlations between attributes and market value.
- Identified missing values and outliers.

## Model Implementation

- **Algorithm Used**: Random Forest Regression. The Random Forest model was chosen due to its ability to handle complex relationships within the data, its robustness against overfitting, and its capability to capture nonlinear interactions between player attributes and market value.
- **Splitting Data**: 80% training, 20% testing.
- **Hyperparameter Tuning**: Applied techniques such as cross-validation to optimize performance.

## Model Evaluation

- **Metrics Used**:
  - Mean Squared Error (MSE)
  - R-squared (R²)
- **Comparison**: Model performance was evaluated against baseline models.

## Deployment

The trained model is deployed as an API using **FastAPI** and is hosted on Render. You can access the deployed API at: [Kal Players Market Value Prediction](https://kal-players-market-value-prediction.onrender.com/), allowing users to input player attributes and receive predicted market values.

## How to Use

You can directly access the deployed API at: [Kal Players Market Value Prediction](https://kal-players-market-value-prediction.onrender.com/).

Alternatively, if you wish to run the project locally:

1. Clone this repository.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn api.app:app --reload
   ```

## Requirements
The project requires the following dependencies:
- pandas
- numpy
- scikit-learn
- joblib
- fastapi
- pathlib
- pydantic
- matplotlib
- uvicorn

## Repository Structure

```
├── api/
│   ├── app.py  # FastAPI Backend
├── data/
│   ├── FIFA17_official.csv  # Raw dataset
│   ├── FIFA17_filtered.csv  # Processed dataset
├── models/  # Trained machine learning models
├── notebooks/
│   ├── EDA.ipynb  # Exploratory Data Analysis
│   ├── modeltraining.ipynb  # Model training
├── src/
│   ├── dataprocessing.py  # Data cleaning and preprocessing
│   ├── trainedmodel.py  # Model loading and inference
├── .gitignore
├── README.md  # Project documentation
├── requirements.txt  # Dependencies
```

## Author

**Kalkidan Zenebe** - Bachelor of Software Engineering, Debre Birhan University.

