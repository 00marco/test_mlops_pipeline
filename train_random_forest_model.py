import pandas as pd
import sqlite3
import numpy as np
import time 
from sklearn.ensemble import RandomForestRegressor
import mlflow
import os

mlflow.sklearn.autolog()
os.environ['MLFLOW_TRACKING_URI'] = 'sqlite:///mlflow.db'


# Connect to the SQLite database
conn = sqlite3.connect('data.db') 
cursor = conn.cursor()


def get_last_100_numbers():
    query = "SELECT score FROM score ORDER BY id DESC LIMIT 101"  
    cursor.execute(query)
    last_100_numbers = cursor.fetchall()
    return [x[0] for x in last_100_numbers if type(x[0]) == float]

def prepare_data(sequences):
    X, y = [], []
    for i in range(len(sequences) - 10):
        # print("X", len(sequences[i:i+10]))
        # print(sequences[i:i+10])
        # print("y")
        # print(sequences[i+10])
        X.append(sequences[i:i+10])
        y.append(sequences[i+10])

    # print("XX", X)
    # print("yy", y)
    return np.array(X), np.array(y)


while True:
    # Get the last 100 numbers from the database
    last_100_numbers = get_last_100_numbers()
    # print("len", len(last_100_numbers), last_100_numbers)
    # Train a Random Forest model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    X, y = prepare_data(last_100_numbers)
    rf_model.fit(X, y)
    time.sleep(10)




