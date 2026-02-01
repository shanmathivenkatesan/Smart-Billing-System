from fastapi import FastAPI
import uuid
from database import get_db
from agents.print_agent import PrintDecisionAgent
from agents.offline_agent import OfflineOnlineAgent
from agents.error_agent import ErrorRecoveryAgent

app = FastAPI()
db = get_db()

print_agent = PrintDecisionAgent()
offline_agent = OfflineOnlineAgent()
error_agent = ErrorRecoveryAgent()

@app.post("/generate_bill")
def generate_bill(amount: float):
    invoice_id = str(uuid.uuid4())[:8]

    if not error_agent.validate_invoice(invoice_id, db):
        return {"error": "Duplicate invoice"}

    online = offline_agent.is_online()
    status = "ONLINE" if online else "OFFLINE"

    db.execute(
        "INSERT INTO invoices VALUES (?, ?, ?, ?)",
        (invoice_id, amount, status, 0 if not online else 1)
    )
    db.commit()

    print_agent.print_invoice(invoice_id)

    return {
        "invoice_id": invoice_id,
        "amount": amount,
        "mode": status
    }

@app.get("/sync")
def sync_data():
    cursor = db.cursor()
    cursor.execute("UPDATE invoices SET synced=1 WHERE synced=0")
    db.commit()
    return {"message": "Offline data synced"}
