# House-price-prediction---ML

## Overview
In this project, the objective is to predict house prices in India based on various features like BHK number, resale, rera, posted by, under construction, bhk or rk, longitude and latitude.The data set that has used in this project has taken from the kaggle [dataset](https://www.kaggle.com/datasets/anmolkumar/house-price-prediction-challenge/data). I carefully worked on feature engineering, data cleaning, and creating visualizations to make the house price prediction models more accurate and robust. I used advanced techniques like fine-tuning the model parameters with GridSearchCV and combining different models together (Bagging, Boosting, Stacking) to make the predictions better.
## How to run?
### Step 1: Data installation
Install dataset from kaggle
### Step 2: Install the requirements
```bash
pip install -r requirements.txt
```
### Step 3: Download the notebook(.ipynb) and run 

### Step 4: Running the Flask App

A Flask application has been added for serving the model predictions via a web interface. To run the Flask app:

1. Navigate to the directory containing the Flask app files.
2. Run the following command to start the server:

```bash
python app.py
```

3. Open your browser and navigate to http://127.0.0.1:5000/ to interact with the app.

## Tech Stack Used
1. Programming Language: Python
2. Data Manipulation: Pandas, NumPy, geopandas
3. Data Visualization: Matplotlib, Seaborn, shaply
4. Machine Learning: Scikit-Learn, XGBoost, Random Forest, etc
5. Model Selection and Tuning: GridSearchCV
6. Ensemble Methods: Bagging, Boosting, Stacking
7. Web Framework: Flask

## Flask App Structure
1. app.py: Contains the code for running the Flask application.
2. templates/index.html: The main HTML page for the web interface.
3. static/styles.css: CSS file for styling the web interface.
