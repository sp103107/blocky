import json
from agents.transaction_validator.validator import validate_transaction
from agents.tokenization_agent.tokenizer import tokenize
from agents.blockchain_recorder.recorder import record_transaction

with open("mock_data/transactions.json") as file:
    transactions = json.load(file)

with open("mock_data/tokens.json") as file:
    token_map = json.load(file)

user_balances = {"Alice": 150, "Bob": 50, "Charlie": 20}

for transaction in transactions:
    if validate_transaction(transaction, user_balances):
        tokenized = tokenize(transaction, token_map)
        record_transaction(tokenized, "blockchain_ledger.json")
