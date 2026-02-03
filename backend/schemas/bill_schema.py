from pydantic import BaseModel

class BillRequest(BaseModel):
    product_id: int
    quantity: int
    total: float
