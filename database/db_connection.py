import sqlite3
import os

# Path to SQLite database file
DB_PATH = os.path.join(os.path.dirname(__file__), "local.db")

def get_connection():
    """Connect to the SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    return conn

def close_connection(conn):
    """Close the SQLite database connection"""
    conn.close()
