def create_bill_table(db):
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id TEXT PRIMARY KEY,
            amount REAL,
            status TEXT
        )
    """)
    db.commit()

def insert_bill(db, bill_id, amount, status):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO bills VALUES (?, ?, ?)",
        (bill_id, amount, status)
    )
    db.commit()

from pydantic import BaseModel

class BillRequest(BaseModel):
    amount: float

