from pydantic import BaseModel, Field
from typing import Optional


class BillRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Total bill amount")
    customer_name: Optional[str] = None
    payment_method: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "amount": 450.75,
                "customer_name": "Ravi Kumar",
                "payment_method": "UPI"
            }
        }
