import csv
import random
from datetime import datetime, timedelta

num_records = 10000
fraud_ratio = 0.1  # 10% fraud

locations = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad"]
device_types = ["Android", "iOS", "Web"]

with open('data/transactions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        'transaction_id','user_id','amount','timestamp','location','device_type',
        'user_age_days','transaction_count_last_1_day','transaction_count_last_1_hour',
        'average_amount_last_7_days','is_kyc_verified','location_distance_from_home_km',
        'is_foreign_device','previous_fraud_count','is_fraud'
    ])
    
    for i in range(1, num_records+1):
        # Randomly assign fraud
        is_fraud = 1 if random.random() < fraud_ratio else 0
        
        # Normal features
        user_age = random.randint(30, 1000)
        transactions_1d = random.randint(0, 20)
        transactions_1h = random.randint(0, 5)
        avg_amount_7d = random.uniform(50, 10000)
        kyc_verified = random.choice([0,1])
        distance_from_home = random.uniform(0, 1000)
        foreign_device = 1 if random.random() < 0.05 else 0
        prev_fraud = random.randint(0, 2)
        amount = random.uniform(10, 50000)
        
        # Make fraud more extreme
        if is_fraud:
            amount *= random.uniform(1.5, 3)  # high amount
            transactions_1h += random.randint(5, 10)
            distance_from_home += random.randint(100, 500)
            foreign_device = 1
            kyc_verified = 0
        
        writer.writerow([
            f"TXN{i:05d}", f"USR{random.randint(1,1000):04d}", round(amount,2),
            (datetime.now() - timedelta(days=random.randint(0,30))).isoformat(),
            random.choice(locations), random.choice(device_types),
            user_age, transactions_1d, transactions_1h,
            round(avg_amount_7d,2), kyc_verified, round(distance_from_home,2),
            foreign_device, prev_fraud, is_fraud
        ])
