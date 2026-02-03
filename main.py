# -------------------------
# IMPORTS
# -------------------------
import sys
from pathlib import Path
import uuid
import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

sys.path.append(str(Path(__file__).parent))

from backend.database import get_db
from backend.models.bill_model import create_bill_table, insert_bill
from backend.models.schemas.bill_schema import BillRequest
from backend.models.schemas.product_schema import ProductRequest

from backend.agents.print_agent import PrintDecisionAgent
from backend.agents.offline_agent import OfflineOnlineAgent
from backend.agents.error_agent import ErrorRecoveryAgent

# -------------------------
# Initialize FastAPI
# -------------------------
app = FastAPI(title="AIAG03 Smart Billing System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Initialize Database & Agents
# -------------------------
db = get_db()
create_bill_table(db)

print_agent = PrintDecisionAgent()
offline_agent = OfflineOnlineAgent()
error_agent = ErrorRecoveryAgent()

# -------------------------
# Schemas
# -------------------------
class LoginRequest(BaseModel):
    username: str
    password: str

# -------------------------
# Test API
# -------------------------
@app.get("/test")
def test_api():
    return {"message": "Frontend connected successfully"}

# -------------------------
# API Endpoints
# -------------------------
@app.post("/generate_bill")
def generate_bill(bill: BillRequest):
    try:
        bill_id = str(uuid.uuid4())
        network = offline_agent.check_network()
        status = "Saved Offline" if not network else print_agent.decide()
        insert_bill(db, bill_id, bill.amount, status)
        return {"bill_id": bill_id, "amount": bill.amount, "status": status, "timestamp": datetime.datetime.now().isoformat()}
    except Exception as e:
        error_agent.handle_error(e)
        return {"error": str(e)}

@app.post("/products")
def add_product(product: ProductRequest):
    try:
        return {"status": "success", "product": product}
    except Exception as e:
        error_agent.handle_error(e)
        return {"error": str(e)}

@app.post("/api/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "1234":
        return {"message": "Login successful", "user": request.username, "token": str(uuid.uuid4())}
    else:
        return {"message": "Invalid credentials"}, 401
