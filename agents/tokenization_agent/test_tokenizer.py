from tokenizer import tokenize

token_map = {"valid": "S1", "insufficient_funds": "S2"}
transaction = {"from": "Alice", "to": "Bob", "amount": 50, "status": "valid"}

print(tokenize(transaction, token_map))
