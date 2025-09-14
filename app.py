from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load('models/supervised_model.pkl')

# Predefined label encoders (must match notebook)
location_encoder = LabelEncoder()
location_encoder.fit(['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Hyderabad'])

device_encoder = LabelEncoder()
device_encoder.fit(['Android', 'iOS', 'Web'])

def preprocess_input(data):
    df = pd.DataFrame([data])

    # Encode categorical columns
    df['location'] = location_encoder.transform(df['location'])
    df['device_type'] = device_encoder.transform(df['device_type'])

    # Convert booleans to integers
    df['is_kyc_verified'] = int(df['is_kyc_verified'].iloc[0])
    df['is_foreign_device'] = int(df['is_foreign_device'].iloc[0])


    # Drop unnecessary columns if present
    df = df.drop(columns=['transaction_id', 'user_id', 'timestamp'], errors='ignore')

    return df

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    processed = preprocess_input(data)
    prediction = model.predict(processed)[0]
    probability = model.predict_proba(processed)[0][1]

    return jsonify({
        'is_fraud': int(prediction),
        'fraud_probability': float(probability)
    })

if __name__ == '__main__':
    app.run(debug=True)

