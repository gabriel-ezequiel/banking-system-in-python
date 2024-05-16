from .Transaction import Transaction


class Withdrawal(Transaction):
    def __init__(self, value: float) -> None:
        self._value = value

    @property
    def value(self) -> float:
        return self._value
    
    def record(self, account) -> None:
        if account.withdraw(self.value):
            account.history.add_transaction(self)
            print(f"Transaction: {self.value} withdrawn")