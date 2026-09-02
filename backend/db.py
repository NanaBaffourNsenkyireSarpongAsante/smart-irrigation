# ============================================================
# DATABASE MODULE - connection and schema
# ============================================================
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name('irrigation.db')


def get_connection():
    return sqlite3.connect(str(DB_PATH))


def init_db():
    conn = get_connection()
    c = conn.cursor()
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        moisture REAL,
        pump_status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()
