import requests

url = "http://127.0.0.1:5000/predict"

transaction = {
    "transaction_id": "TXN001",
    "user_id": "USR001",
    "amount": 10000,
    "timestamp": "2025-09-14T22:10:00",
    "location": "Delhi",
    "device_type": "Android",
    "user_age_days": 400,
    "transaction_count_last_1_day": 10,
    "transaction_count_last_1_hour": 2,
    "average_amount_last_7_days": 3000,
    "is_kyc_verified": True,
    "location_distance_from_home_km": 120.5,
    "is_foreign_device": False,
    "previous_fraud_count": 1
}

response = requests.post(url, json=transaction)
print(response.json())
