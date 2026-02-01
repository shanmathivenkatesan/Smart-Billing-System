import time
import random

class PrintDecisionAgent:
    def print_invoice(self, invoice_id):
        printers = ["Printer_A", "Printer_B"]
        selected_printer = printers[0]

        print(f"[PrintAgent] Selected {selected_printer}")
        time.sleep(1)

        if random.choice([True, False]):
            print(f"[PrintAgent] Printed invoice {invoice_id}")
            return True
        else:
            print("[PrintAgent] Print failed → Switching printer")
            print(f"[PrintAgent] Printed using {printers[1]}")
            return True
