# AI_Predictive_Models_for_Credit_Underwriting

Overview
-------------
This project utilizes AI-based predictive models to enhance the accuracy and efficiency of credit underwriting. By analyzing historical financial data, the model predicts the likelihood of a customer defaulting on a loan, helping financial institutions make more informed decisions.

About
---------------
Predictive Modeling: Uses machine learning algorithms to predict credit risk based on historical data.
Data Preprocessing: Includes data cleaning, feature selection, and data transformation for model training.
Model Evaluation: Implements various evaluation metrics (accuracy, precision, recall, F1-score, ROC curve) to assess model performance.
Visualizations: Provides clear visualizations to help understand model performance and decision boundaries.
Requirements
Python 3.x
Libraries:
pandas
numpy
scikit-learn
matplotlib
seaborn

Features
-------------------------------------
Two apps for flexibility:

*Flask App: A traditional web application.*

*Streamlit App: A modern, interactive dashboard for streamlined predictions.*

Input preprocessing (e.g., log transformations, one-hot encoding).
A pre-trained machine learning model (model.pkl) for prediction.

Requirements 
---------------------
Flask
Streamlit
NumPy
scikit-learn
Pickle (standard library)
To install the necessary libraries, use the following command:
Copy code
pip install -r requirements.txt

Setup
---------------
Clone the repository to your local machine:
Copy code
git clone https://github.Aayushipandey54/AI_Predictive_Models_for_Credit_Underwriting.git
cd AI_Predictive_Models_for_Credit_Underwriting
Install required dependencies:
Copy code
pip install -r requirements.txt


Data
------------
The project uses historical credit data, including:
Loan amount
Income
Credit score
Employment history
Age
... and other relevant features.
Note: Ensure you have the correct dataset path configured in the script.

How It Works
---------------
1. Data Preprocessing
Cleaning the dataset by handling missing values, outliers, and categorical data encoding.
Splitting the data into training and testing sets.
2. Model Training
Train machine learning models such as:
Logistic Regression
Decision Trees
Random Forests
Neural Networks
3. Model Evaluation
Evaluate the model using cross-validation, confusion matrix, and various classification metrics (accuracy, recall, precision, etc.).
4. Predictions
Generate predictions on unseen test data for credit risk assessment.
Usage
To train and evaluate the models:
Run the main Python script:
Copy code
python main.py


The script will load the dataset, preprocess the data, train the models, and output the evaluation metrics.
Model Results
After running the model, you will get:
Accuracy scores of each model
Confusion matrix for error analysis
ROC-AUC curve visualization
Contributing
Fork the repository
Create a new branch
Make changes and commit them
Push to your forked repository
Create a pull request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
-----------------------
References for credit underwriting methodologies and machine learning techniques can be found in the documentation.

Notes
------------
Ensure the model.pkl file is in the same directory as app.py for both Flask and Streamlit applications.
If deploying to a cloud platform, adjust configurations for static files and port settings.
For any issues, raise them in the repository.

