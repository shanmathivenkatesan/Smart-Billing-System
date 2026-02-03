from backend.database import get_db

def create_products_table():
    db = get_db()
    db.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    """)
    db.commit()
    db.close()

def add_product(name: str, price: float):
    db = get_db()
    db.execute("INSERT INTO products(name, price) VALUES (?, ?)", (name, price))
    db.commit()
    db.close()

def get_products():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    db.close()
    return [{"id": p[0], "name": p[1], "price": p[2]} for p in products]
