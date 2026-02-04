"""
Offline/Online Agent
Simulates checking if system is online or offline
Makes autonomous decision about connectivity
"""
import random

class OfflineOnlineAgent:
    """
    Agent that checks if the system is online or offline
    Simulates internet connectivity check
    """
    
    def decide(self, bill):
        """
        Decide if system is currently online or offline
        
        Rules:
        - 80% chance we're online (normal operation)
        - 20% chance we're offline (network issues)
        
        Args:
            bill: The bill (not used, but kept for consistency)
            
        Returns:
            Dictionary with connectivity status
        """
        
        # Simulate network check
        # In real life, this would ping a server or check internet connection
        is_online = random.random() < 0.8  # 80% chance online
        
        if is_online:
            return {
                "is_online": True,
                "status": "ONLINE",
                "reason": "Internet connection stable",
                "features": ["Cloud sync", "Email receipts", "Online payments"],
                "agent": "OfflineOnlineAgent"
            }
        else:
            return {
                "is_online": False,
                "status": "OFFLINE",
                "reason": "No internet - operating in offline mode",
                "features": ["Local storage only", "Print receipts"],
                "agent": "OfflineOnlineAgent"
            }
