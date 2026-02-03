from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import datetime

# -------------------------
# App init
# -------------------------
app = FastAPI(title="AIAG03 Smart Billing System")

# -------------------------
# CORS (Frontend connect aaga)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # frontend allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Schemas
# -------------------------
class LoginRequest(BaseModel):
    email: str
    password: str

class BillRequest(BaseModel):
    amount: float

# -------------------------
# TEST API (connection check)
# -------------------------
@app.get("/test")
def test_api():
    return {"message": "Backend is running successfully"}

# -------------------------
# LOGIN API (Frontend uses this)
# -------------------------
from fastapi import HTTPException

@app.post("/api/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "1234":
        token = str(uuid.uuid4())  # generate dummy token
        return {
            "message": "Login successful",
            "user": request.username,
            "token": token
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


# -------------------------
# BILL GENERATE API
# -------------------------
@app.post("/generate_bill")
def generate_bill(bill: BillRequest):
    bill_id = str(uuid.uuid4())

    return {
        "bill_id": bill_id,
        "amount": bill.amount,
        "status": "Generated",
        "timestamp": datetime.datetime.now().isoformat()
    }
