def tokenize(transaction, token_map):
    transaction["status"] = token_map.get("valid", "unknown")
    return transaction
