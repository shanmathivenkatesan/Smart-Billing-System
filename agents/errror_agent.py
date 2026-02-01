class ErrorRecoveryAgent:
    def validate_invoice(self, invoice_id, db):
        cursor = db.cursor()
        cursor.execute("SELECT id FROM invoices WHERE id=?", (invoice_id,))
        return cursor.fetchone() is None
