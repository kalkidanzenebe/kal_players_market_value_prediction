
# Football Player Value Prediction

## Problem Statement

In football, player market value is influenced by a combination of factors such as age, performance statistics, club reputation, and potential. However, determining the exact market value of a player remains subjective and can vary across teams, agents, and media outlets. The goal of this project is to build a machine learning-based prediction system that accurately estimates a player's market value based on these influential features.

## Project Structure

/pmv │── api/ │ ├── app.py # FastAPI backend to handle requests and predictions │── static/ │ ├── index.html # Frontend HTML structure │ ├── style.css # CSS styling for the frontend │ ├── script.js # JavaScript to interact with the backend │── models/ # Directory containing trained machine learning models │── notebooks/ # Jupyter notebooks for exploratory data analysis (EDA) and model training │── src/ │ ├── dataprocessing.py # Data processing utilities │ ├── trainedmodel.py # Code for loading and predicting with the trained models │── data/ # Contains FIFA17 dataset and filtered version │── .gitignore # Git ignore file to exclude unnecessary files from version control │── .gitattributes # Git attributes to define project-specific settings │── README.md # Project overview and setup instructions │──


## Requirements

- Python 3.x
- FastAPI
- Uvicorn
- scikit-learn
- pandas
- numpy
- pathlib
- other dependencies listed in `requirements.txt`

Install the required Python dependencies by running:

##### Setup and Running the Application

1. Clone the repository:

- git clone <repository_url> cd <repository_directory>


2. Install dependencies:
- pip install -r requirements.txt


3. Start the FastAPI backend:(using one of the commands and run in the terminal and start the api)
- uvicorn api.app:app --reload
- or you an you can use python api/app.py


4. Open `static/index.html` in your browser to access the frontend.

## Features

- **Prediction Model:** Predicts a football player's market value based on various features such as age, potential, club, nationality, and performance statistics.
- **User Interface:** Simple frontend to allow users to input player information and see the predicted value.

## Usage

1. On the frontend (`index.html`), input the player's features such as age, club, position, and performance stats.
2. Submit the form, which sends a request to the backend.
3. The FastAPI backend processes the request and responds with the predicted value, which is displayed on the frontend.

## Contributing

Feel free to fork the repository and contribute. Open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.
