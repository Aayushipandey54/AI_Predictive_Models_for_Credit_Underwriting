import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit Layout for Home Page
def home_page():
    st.title("🚀 Loan Prediction System")
    st.markdown("### 📋 **Welcome to the Loan Prediction System!**")
    st.markdown("""This tool helps you predict whether your loan application will be approved or rejected based on a variety of personal and financial factors. Fill in your details and let the system predict your loan status with an accurate machine learning model.""")

    # Add an image to the home page
    st.image("loan.png", caption="Loan Prediction System", use_column_width=True)

    st.markdown("### 🛠️ Project Overview")
    st.markdown("""
        This project was developed as part of my **AI internship** at **Infosys Springboard**. The objective was to build a **Loan Prediction System** that uses machine learning to predict whether a loan application will be approved or rejected based on various parameters like personal and financial details of the applicant.
        The system takes the user's input and processes it through a pre-trained model to deliver a prediction about the loan status. We used algorithms like **Logistic Regression** and **Decision Trees** for accurate predictions.
    """)
    
    # Button to navigate to the prediction page
    if st.button("🔮 Go to Prediction Page"):
        st.session_state.page = "Prediction"

# Streamlit Layout for About Us Page
def about_us_page():
    st.title("📖 About Us")
    st.markdown("""**Our Mission**: We aim to provide **innovative, efficient, and easy-to-use** financial tools that assist individuals in making better financial decisions. Our mission is to simplify complex loan application processes using advanced technology like **Machine Learning** and **AI**.""")

    # About Me Section
    st.markdown("### 👩‍💻 About Me")
    st.markdown("""
        **Aayushi Pandey** - I am currently working as an **AI Intern** at **Infosys Springboard**. This project, which focuses on predicting loan approvals, was developed during my internship as part of a real-world application of machine learning in the finance sector.
        
        During my internship, I worked on **data preprocessing**, **model training**, and **prediction optimization** using various machine learning algorithms. This project is a great example of how **AI** can be applied to solve everyday financial problems.
    """)

    # Add an image to the About Us page
    st.image("About.jpg", caption="AI Intern Project", use_column_width=True)

    # Footer specific to About Us page
    footer()

# Streamlit Layout for Prediction Page
def prediction_page():
    st.title("🚀 Loan Prediction System")
    st.markdown("### 📋 Enter Loan Application Details to Predict Your Loan Status!")

    # User input fields for prediction
    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    married = st.selectbox("💍 Marital Status", ["Yes", "No"])
    dependents = st.selectbox("👨‍👩‍👧 Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("🎓 Education", ["Graduate", "Not Graduate"])
    employed = st.selectbox("💼 Self Employed", ["Yes", "No"])
    credit = st.slider("📊 Credit History", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
    area = st.selectbox("🏠 Property Area", ["Urban", "Semiurban", "Rural"])
    ApplicantIncome = st.slider("💰 Applicant Income", min_value=1000, max_value=100000, step=1000, value=5000)
    CoapplicantIncome = st.slider("🤝 Coapplicant Income", min_value=0, max_value=100000, step=1000, value=0)
    LoanAmount = st.slider("🏦 Loan Amount", min_value=1, max_value=100000, step=10, value=100)
    Loan_Amount_Term = st.select_slider("📅 Loan Amount Term (in days)", options=[360, 180, 240, 120], value=360)

    # Preprocess input data and make predictions
    def preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term):
        male = 1 if gender == "Male" else 0
        married_yes = 1 if married == "Yes" else 0
        if dependents == '1':
            dependents_1, dependents_2, dependents_3 = 1, 0, 0
        elif dependents == '2':
            dependents_1, dependents_2, dependents_3 = 0, 1, 0
        elif dependents == "3+":
            dependents_1, dependents_2, dependents_3 = 0, 0, 1
        else:
            dependents_1, dependents_2, dependents_3 = 0, 0, 0

        not_graduate = 1 if education == "Not Graduate" else 0
        employed_yes = 1 if employed == "Yes" else 0
        semiurban = 1 if area == "Semiurban" else 0
        urban = 1 if area == "Urban" else 0

        ApplicantIncomelog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome + CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)

        return [
            credit, ApplicantIncomelog, LoanAmountlog, Loan_Amount_Termlog, totalincomelog,
            male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes, semiurban, urban
        ]

    if st.button("🔮 Predict Loan Status"):
        features = preprocess_data(gender, married, dependents, education, employed, credit, area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term)

        # Prediction
        prediction = model.predict([features])

        # Convert prediction to human-readable format
        if prediction == "N":
            prediction = "No"
            st.error("⚠️ Loan Status: **Rejected**")
            st.markdown("### ☠️ Danger! Your loan application has been **rejected**.")
            st.markdown("""
            **Possible reasons:**
            - Low credit history score
            - Insufficient income for the loan amount requested
            - High debt-to-income ratio
            - Other potential risk factors

            **Critical suggestions:**
            - **Immediate action:** Improve your credit score by paying off existing debts.
            - Consider **reducing your loan amount** or opting for a longer repayment term.
            - **Reassess your finances** and improve your overall financial health before reapplying.

            *Take care to address these issues before trying again!*
            """)
        else:
            prediction = "Yes"
            st.success("✅ Loan Status: **Approved**")
            st.markdown("### 🎉 Congratulations! Your loan application is likely approved!")
            st.balloons()
            st.markdown("""
            **Key highlights of your application:**
            - Good credit history score
            - Sufficient income to cover loan repayment
            - Positive factors supporting your loan approval

            Enjoy your financial journey with the new loan!
            """)

# Footer for About Us Page
def footer():
    st.markdown("---")
    st.markdown("### 🌐 Connect with us")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/aayushi-pandey-7b0b5b1b2/)")
    st.markdown("[GitHub](https://github.com/Aayushipandey54?tab=repositories/)")
    st.markdown("📧 Email: pandeyaayushi358@gmail.com")

# Sidebar Layout Design Enhancement
def sidebar_layout():
    st.sidebar.title("🔧 Menu")
    st.sidebar.markdown("### Choose a Page")
    
    menu = st.sidebar.radio(
        "Go to", ["Home", "About Us", "Prediction"]
    )
    
    if menu == "Home":
        home_page()
    elif menu == "Prediction":
        prediction_page()
    else:
        about_us_page()

# Set initial page state if not defined
sidebar_layout()
