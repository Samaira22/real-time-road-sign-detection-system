import sqlite3
import time

DB_PATH = "storage/detections.db"
LOG_COOLDOWN = 3

last_logged = {}


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_detection(class_name, confidence):
    current_time = time.time()
    last_time = last_logged.get(class_name, 0)

    if current_time - last_time < LOG_COOLDOWN:
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO detections (class_name, confidence)
        VALUES (?, ?)
    """, (class_name, confidence))

    conn.commit()
    conn.close()

    last_logged[class_name] = current_time


def get_detections():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT class_name, confidence, timestamp
        FROM detections
        ORDER BY timestamp DESC
    """)

    data = cursor.fetchall()
    conn.close()

    return data