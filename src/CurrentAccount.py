from .Account import Account

class CurrentAccount(Account):
    def __init__(self, number: int, customer, limit: float = 500, withdraw_limit: int = 3):
        super().__init__(number, customer)
        self._LIMIT = limit
        self._WITHDRAWAL_LIMIT = withdraw_limit
        self._withdrawal_number = 0

    def withdraw(self, value) -> bool:
        if (value > 0):
            if (self._WITHDRAWAL_LIMIT <= self._withdrawal_number):
                print("Withdrawal limit reached")
                return False
            elif (self._LIMIT < value):
                print(f"Exceeded withdrawal limit of R$ {self._LIMIT:.2f}")
                return False
            elif (self._balance >= value):
                self._balance -= value
                self._withdrawal_number += 1
                return True
            else:
                print("Insufficient balance")
                return False
        else:
            print("Invalid value")
            return False
    

        