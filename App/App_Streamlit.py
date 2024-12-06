# This the app using Streamlit

import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit Layout
st.title("Loan Prediction System")

st.header("Enter Loan Application Details")

# Gender
gender = st.selectbox("Gender", ["Male", "Female"])

# Married
married = st.selectbox("Marital Status", ["Yes", "No"])

# Dependents
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])

# Education
education = st.selectbox("Education", ["Graduate", "Not Graduate"])

# Employment Status
employed = st.selectbox("Self Employed", ["Yes", "No"])

# Credit History
credit = st.number_input("Credit History", min_value=0.0, max_value=1.0, step=0.01)

# Property Area
area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Applicant Income
ApplicantIncome = st.number_input("Applicant Income", min_value=1000, max_value=100000, value=5000)

# Coapplicant Income
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0, max_value=100000, value=0)

# Loan Amount
LoanAmount = st.number_input("Loan Amount", min_value=1, max_value=1000, value=100)

# Loan Amount Term
Loan_Amount_Term = st.selectbox("Loan Amount Term", [360, 180, 240, 120])

# Preprocess input data and make predictions
def preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term):
    # Gender
    male = 1 if gender == "Male" else 0

    # Married
    married_yes = 1 if married == "Yes" else 0

    # Dependents
    if dependents == '1':
        dependents_1, dependents_2, dependents_3 = 1, 0, 0
    elif dependents == '2':
        dependents_1, dependents_2, dependents_3 = 0, 1, 0
    elif dependents == "3+":
        dependents_1, dependents_2, dependents_3 = 0, 0, 1
    else:
        dependents_1, dependents_2, dependents_3 = 0, 0, 0  

    # Education
    not_graduate = 1 if education == "Not Graduate" else 0

    # Employed
    employed_yes = 1 if employed == "Yes" else 0

    # Area
    semiurban = 1 if area == "Semiurban" else 0
    urban = 1 if area == "Urban" else 0

    # Apply log transformation
    ApplicantIncomelog = np.log(ApplicantIncome)
    totalincomelog = np.log(ApplicantIncome + CoapplicantIncome)
    LoanAmountlog = np.log(LoanAmount)
    Loan_Amount_Termlog = np.log(Loan_Amount_Term)

    # Return preprocessed features
    return [
        credit, ApplicantIncomelog, LoanAmountlog, Loan_Amount_Termlog, totalincomelog,
        male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes, semiurban, urban
    ]

# When the "Predict" button is clicked
if st.button("Predict Loan Status"):
    features = preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term)
    
    # Prediction
    prediction = model.predict([features])

    # Convert prediction to human-readable format
    if prediction == "N":
        prediction = "No"
    else:
        prediction = "Yes"

    st.subheader(f"Loan Status: {prediction}")
