from faker import Faker
import pandas as pd
import os

pwd = os.getcwd()

fake = Faker()

users = []

for _ in range(100):
    user = {
        'name': fake.name(),
        'email': fake.email(),
        'age': fake.random_int(min=18, max=65),
        'city': fake.city(),
        'job': fake.job()
    }
    users.append(user)


print("Users Created")
    
    
user_dataset = pd.DataFrame(users)


user_dataset.to_csv(f'{pwd}\\user_data.csv', index=False)
