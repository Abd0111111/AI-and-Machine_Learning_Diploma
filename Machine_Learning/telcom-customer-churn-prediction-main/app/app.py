from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from pathlib import Path


def load_model():
    model_path = Path(__file__).parent.parent / "model/log_reg_pipeline.joblib"
    model = joblib.load(model_path)
    return model


def extract_data(data):
    gender = data.get('gender')
    SeniorCitizen = 'Yes' if str(data.get('SeniorCitizen')) in ('1', 'Yes') else 'No'  # map to Yes/No like training data
    Partner = data.get('Partner')
    Dependents = data.get('Dependents')
    tenure = data.get('tenure')
    PhoneService = data.get('PhoneService')
    MultipleLines = data.get('MultipleLines')
    InternetService = data.get('InternetService')
    OnlineSecurity = data.get('OnlineSecurity')
    OnlineBackup = data.get('OnlineBackup')
    DeviceProtection = data.get('DeviceProtection')
    TechSupport = data.get('TechSupport')
    StreamingTV = data.get('StreamingTV')
    StreamingMovies = data.get('StreamingMovies')
    Contract = data.get('Contract')
    PaperlessBilling = data.get('PaperlessBilling')
    PaymentMethod = data.get('PaymentMethod')
    MonthlyCharges = data.get('MonthlyCharges')
    TotalCharges = data.get('TotalCharges')

    df = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [tenure],
        "PhoneService": [PhoneService],
        "MultipleLines": [MultipleLines],
        "InternetService": [InternetService],
        "OnlineSecurity": [OnlineSecurity],
        "OnlineBackup": [OnlineBackup],
        "DeviceProtection": [DeviceProtection],
        "TechSupport": [TechSupport],
        "StreamingTV": [StreamingTV],
        "StreamingMovies": [StreamingMovies],
        "Contract": [Contract],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [PaymentMethod],
        "MonthlyCharges": [MonthlyCharges],
        "TotalCharges": [TotalCharges]
    })

    return df


app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = extract_data(data)
    model = load_model()
    model_predict = model.predict(df)[0]

    if model_predict == 1:
        return jsonify({'message': 'This customer is likely to churn!', 'churn': True})
    else:
        return jsonify({'message': 'This customer is not likely to churn.', 'churn': False})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)