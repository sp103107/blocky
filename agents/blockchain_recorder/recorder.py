import json

def record_transaction(transaction, ledger_file):
    try:
        with open(ledger_file, "r") as file:
            ledger = json.load(file)
    except FileNotFoundError:
        ledger = []

    ledger.append(transaction)

    with open(ledger_file, "w") as file:
        json.dump(ledger, file, indent=4)
