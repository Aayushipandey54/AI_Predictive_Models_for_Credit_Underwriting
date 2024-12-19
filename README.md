# 🚀 AI Predictive Models for Credit Underwriting

**Leverage AI-powered predictive models to revolutionize credit underwriting and streamline decision-making.**

---

## 📜 Overview

This project enhances the accuracy and efficiency of credit underwriting using AI-based predictive models. By analyzing historical financial data, the system predicts the likelihood of a customer defaulting on a loan, empowering financial institutions with data-driven insights.

---

## 📂 Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [How It Works](#how-it-works)
6. [Usage](#usage)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)

---

## 🛠️ About

- **Predictive Modeling**: Leverages machine learning algorithms to predict credit risk.
- **Data Preprocessing**: Includes cleaning, feature selection, and transformation.
- **Model Evaluation**: Implements metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
- **Visualizations**: Offers clear visual insights into model performance and decision boundaries.

---

## 🌟 Features

- 🌐 **Two Apps**:
  - Flask App: Traditional web application.
  - Streamlit App: Interactive dashboard for predictions.
- 🔄 **Input Preprocessing**: Includes log transformations and one-hot encoding.
- 📊 **Pre-trained Model**: A machine learning model (`model.pkl`) ready for predictions.

---

## 💻 Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `streamlit`
  - `flask`

Install all dependencies using:

```bash
pip install -r requirements.txt
⚙️ Setup
Clone the repository:
bash
Copy code
git clone https://github.com/Aayushipandey54/AI_Predictive_Models_for_Credit_Underwriting.git
cd AI_Predictive_Models_for_Credit_Underwriting
Install dependencies:
bash
Copy code
pip install -r requirements.txt
⚡ How It Works
1️⃣ Data Preprocessing
Clean the dataset (handle missing values and outliers).
Encode categorical variables.
Split data into training and testing sets.
2️⃣ Model Training
Trains the following models:

Logistic Regression
Decision Trees
Random Forests
Neural Networks
3️⃣ Model Evaluation
Evaluate models using:

Confusion Matrix
Cross-validation
Accuracy, Recall, Precision, F1-Score, and ROC-AUC.
4️⃣ Predictions
Generate predictions on unseen data for credit risk assessment.

🛠️ Usage
To train and evaluate the models, run:

bash
Copy code
python main.py
For predictions, use either:

Flask App:

bash
Copy code
flask run
Streamlit App:

bash
Copy code
streamlit run app.py
📈 Results
Model Accuracy: Displays performance metrics for all trained models.
Confusion Matrix: Helps analyze errors.
ROC-AUC Curve: Provides visualization of model performance.
🤝 Contributing
Fork the repository.
Create a new branch for your feature:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add feature"
Push your changes:
bash
Copy code
git push origin feature-name
Create a pull request.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
References for credit underwriting methodologies.
Resources on machine learning techniques.
csharp
Copy code

You can copy this Markdown file directly and use it as your `README.md` on GitHub.
