import requests

class OfflineOnlineAgent:
    def is_online(self):
        try:
            requests.get("https://google.com", timeout=2)
            return True
        except:
            return False
