from datetime import datetime


class History:
    def __init__(self) -> None:
        self._transactions = []

    @property
    def transactions(self) -> list:
        return self._transactions
    
    def add_transaction(self, transaction) -> None:
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.now(),
            }
        )