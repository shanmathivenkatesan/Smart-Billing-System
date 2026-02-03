from backend.database import get_db

def create_bill_table():
    db = get_db()
    db.execute("""
    CREATE TABLE IF NOT EXISTS bills(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER,
        total REAL
    )
    """)
    db.commit()
    db.close()

def insert_bill(product_id: int, quantity: int, total: float):
    db = get_db()
    db.execute("INSERT INTO bills(product_id, quantity, total) VALUES (?, ?, ?)",
               (product_id, quantity, total))
    db.commit()
    db.close()
