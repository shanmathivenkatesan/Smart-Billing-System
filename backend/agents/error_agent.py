"""
Error Detection Agent
Detects errors like duplicate bills
Makes autonomous decisions about data quality
"""

class ErrorDetectionAgent:
    """
    Agent that detects billing errors
    Main job: Find duplicate bills
    """
    
    def decide(self, current_bill, all_bills):
        """
        Check if this bill is a duplicate
        
        Rules:
        - Compare current bill with recent bills
        - If same total and similar timestamp, it's likely a duplicate
        
        Args:
            current_bill: The bill we're checking
            all_bills: All previous bills in storage
            
        Returns:
            Dictionary with error status
        """
        
        # If this is the first bill, no duplicates possible
        if len(all_bills) == 0:
            return {
                "has_error": False,
                "message": "No errors detected",
                "agent": "ErrorDetectionAgent"
            }
        
        # Check last 5 bills for duplicates
        recent_bills = all_bills[-5:] if len(all_bills) > 5 else all_bills
        
        current_total = current_bill["total"]
        current_items_count = len(current_bill["items"])
        
        for old_bill in recent_bills:
            # Check if totals match and item count matches
            if (old_bill["total"] == current_total and 
                len(old_bill["items"]) == current_items_count):
                
                return {
                    "has_error": True,
                    "error_type": "DUPLICATE",
                    "message": f"Possible duplicate of {old_bill['bill_id']}",
                    "agent": "ErrorDetectionAgent"
                }
        
        # No duplicates found
        return {
            "has_error": False,
            "message": "No errors detected",
            "agent": "ErrorDetectionAgent"
        }
```

---

### 📂 backend/requirements.txt
```
fastapi==0.104.1
uvicorn==0.24.0
