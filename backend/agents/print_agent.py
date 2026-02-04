"""
Print Decision Agent
Decides whether to print a physical receipt or not
Uses simple rules (this is the "AI" part)
"""
import random

class PrintDecisionAgent:
    """
    Agent that decides if we should print the receipt
    Makes autonomous decisions based on simple rules
    """
    
    def decide(self, bill):
        """
        Decide whether to print this bill
        
        Rules:
        1. If bill total > 100, always print (important transaction)
        2. Otherwise, randomly decide (simulates printer availability)
        
        Args:
            bill: The bill to decide about
            
        Returns:
            Dictionary with decision and reason
        """
        
        total = bill["total"]
        
        # Rule 1: High-value bills always get printed
        if total > 100:
            return {
                "should_print": True,
                "reason": f"High-value bill (₹{total} > ₹100)",
                "agent": "PrintDecisionAgent"
            }
        
        # Rule 2: For lower amounts, simulate printer availability
        # 60% chance printer is available
        printer_available = random.random() < 0.6
        
        if printer_available:
            return {
                "should_print": True,
                "reason": "Printer available",
                "agent": "PrintDecisionAgent"
            }
        else:
            return {
                "should_print": False,
                "reason": "Printer busy - sending digital receipt",
                "agent": "PrintDecisionAgent"
            }
