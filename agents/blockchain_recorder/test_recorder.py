from recorder import record_transaction

transaction = {"from": "Alice", "to": "Bob", "amount": 50, "status": "S1"}
ledger_file = "blockchain_ledger.json"

record_transaction(transaction, ledger_file)
print(f"Transaction recorded in {ledger_file}")
