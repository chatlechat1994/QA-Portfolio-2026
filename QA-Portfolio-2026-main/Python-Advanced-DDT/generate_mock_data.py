import pandas as pd
from faker import Faker
import os

fake = Faker()

def generate_data(records=50):
    data = []
    for i in range(1, records + 1):
        data.append({
            "id": i,
            "name": fake.name(),
            "email": fake.email(),
            "status": "active"
        })
    
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/test_data.csv', index=False)
    print(f"✅ Created {records} records in data/test_data.csv")

if __name__ == "__main__":
    generate_data()