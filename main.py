# main.py

import sys
from pathlib import Path

# Helps Python & Pylance find backend folder
sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI
import uuid
import datetime

# -------------------------
# Database & Schemas
# -------------------------
from backend.database import get_db
from backend.models.bill_model import create_bill_table, insert_bill
from backend.models.schemas.bill_schema import BillRequest
from backend.models.schemas.product_schema import ProductRequest

# -------------------------
# Agents
# -------------------------
from backend.agents.print_agent import PrintDecisionAgent
from backend.agents.offline_agent import OfflineOnlineAgent
from backend.agents.error_agent import ErrorRecoveryAgent

# -------------------------
# Initialize FastAPI app
# -------------------------
app = FastAPI(title="AIAG03 Smart Billing System")

# -------------------------
# Initialize Database
# -------------------------
db = get_db()
create_bill_table(db)

# -------------------------
# Initialize Agents
# -------------------------
print_agent = PrintDecisionAgent()
offline_agent = OfflineOnlineAgent()
error_agent = ErrorRecoveryAgent()

# -------------------------
# API Endpoints
# -------------------------

@app.post("/generate_bill")
def generate_bill(bill: BillRequest):
    try:
        bill_id = str(uuid.uuid4())

        network = offline_agent.check_network()
        if not network:
            status = "Saved Offline"
        else:
            status = print_agent.decide()

        insert_bill(db, bill_id, bill.amount, status)

        return {
            "bill_id": bill_id,
            "amount": bill.amount,
            "status": status,
            "timestamp": datetime.datetime.now().isoformat()
        }

    except Exception as e:
        error_agent.handle_error(e)
        return {"error": str(e)}


@app.post("/products")
def add_product(product: ProductRequest):
    try:
        # TODO: insert_product(db, product)
        return {
            "status": "success",
            "product": product
        }

    except Exception as e:
        error_agent.handle_error(e)
        return {"error": str(e)}