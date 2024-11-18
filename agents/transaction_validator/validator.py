def validate_transaction(transaction, user_balances):
    sender = transaction["from"]
    amount = transaction["amount"]
    return user_balances.get(sender, 0) >= amount
