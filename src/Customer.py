class Customer:
    def __init__(self, adress: str) -> None:
        self.adress = adress
        self.accounts = []

    def perform_transaction(self, account, transaction):
        transaction.record(account)

    def add_account(self, account) -> None:
        self.accounts.append(account)