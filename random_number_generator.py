import random
import sqlite3
import time


conn = sqlite3.connect('data.db')
cursor = conn.cursor()

while True:
    time.sleep(1)
    number = random.random()
    cursor.execute('''CREATE TABLE IF NOT EXISTS score (
                    id INTEGER PRIMARY KEY,
                    score REAL NOT NULL)''')
    cursor.execute("INSERT INTO score (score) VALUES (?)", (number,))
    conn.commit()
    print(f"inserted {number}")