class ErrorRecoveryAgent:
    def handle_error(self, error_msg):
        print("Error:", error_msg)
        return {"status": "error", "message": error_msg}
