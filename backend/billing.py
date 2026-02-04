"""
Billing Routes - Handles bill generation
Simple and easy to understand
"""
from fastapi import APIRouter
from datetime import datetime
import random
from agents.agent_manager import AgentManager

router = APIRouter()

# Initialize agent manager
agent_manager = AgentManager()

# Simple in-memory storage for bills (acts as our database)
bills_storage = []

@router.post("/generate-bill")
def generate_bill():
    """
    Generate a new bill with random items
    All agents will make autonomous decisions about this bill
    """
    
    # Step 1: Create a bill with random items
    bill_id = f"BILL-{random.randint(1000, 9999)}"
    
    # Some sample grocery items
    items = [
        {"name": "Milk", "price": 50, "qty": 1},
        {"name": "Bread", "price": 30, "qty": 2},
        {"name": "Eggs", "price": 60, "qty": 1},
        {"name": "Rice", "price": 120, "qty": 1},
    ]
    
    # Pick 2-3 random items
    selected_items = random.sample(items, random.randint(2, 3))
    
    # Calculate total
    total = sum(item["price"] * item["qty"] for item in selected_items)
    
    # Create bill object
    bill = {
        "bill_id": bill_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": selected_items,
        "total": total
    }
    
    # Step 2: Let all agents make decisions about this bill
    agent_decisions = agent_manager.process_bill(bill, bills_storage)
    
    # Step 3: Store the bill
    bills_storage.append(bill)
    
    # Step 4: Return bill + agent decisions
    return {
        "bill": bill,
        "agent_decisions": agent_decisions
    }

@router.get("/bills")
def get_all_bills():
    """Get all bills (for debugging)"""
    return {"bills": bills_storage, "total": len(bills_storage)}
