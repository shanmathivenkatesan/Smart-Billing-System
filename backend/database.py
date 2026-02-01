import sqlite3

def get_db():
    conn = sqlite3.connect("billing.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id TEXT PRIMARY KEY,
            amount REAL,
            status TEXT,
            synced INTEGER
        )
    """)
    return conn
