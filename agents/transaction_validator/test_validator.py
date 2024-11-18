from validator import validate_transaction

user_balances = {"Alice": 150, "Bob": 50, "Charlie": 20}
transaction = {"from": "Alice", "to": "Bob", "amount": 50}

print(validate_transaction(transaction, user_balances))
