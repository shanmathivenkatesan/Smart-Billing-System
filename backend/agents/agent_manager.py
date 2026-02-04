"""
Agent Manager - Coordinates all AI agents
Each agent makes independent decisions
"""
from agents.print_agent import PrintDecisionAgent
from agents.offline_agent import OfflineOnlineAgent
from agents.error_agent import ErrorDetectionAgent

class AgentManager:
    """
    Manages all AI agents
    Each agent is independent and makes its own decisions
    """
    
    def __init__(self):
        # Initialize all three agents
        self.print_agent = PrintDecisionAgent()
        self.offline_agent = OfflineOnlineAgent()
        self.error_agent = ErrorDetectionAgent()
    
    def process_bill(self, bill, bills_storage):
        """
        Send bill to all agents and collect their decisions
        
        Args:
            bill: The current bill
            bills_storage: All previous bills (for duplicate check)
        
        Returns:
            Dictionary with all agent decisions
        """
        
        # Each agent independently decides
        print_decision = self.print_agent.decide(bill)
        online_decision = self.offline_agent.decide(bill)
        error_decision = self.error_agent.decide(bill, bills_storage)
        
        # Combine all decisions
        return {
            "print_decision": print_decision,
            "online_decision": online_decision,
            "error_decision": error_decision,
            "summary": self._create_summary(print_decision, online_decision, error_decision)
        }
    
    def _create_summary(self, print_dec, online_dec, error_dec):
        """Create a simple text summary of all decisions"""
        summary = []
        
        if print_dec["should_print"]:
            summary.append("Will print receipt")
        else:
            summary.append("No printing (digital only)")
        
        if online_dec["is_online"]:
            summary.append("System online")
        else:
            summary.append("System offline")
        
        if error_dec["has_error"]:
            summary.append(f"ERROR: {error_dec['message']}")
        else:
            summary.append("No errors")
        
        return " | ".join(summary)
