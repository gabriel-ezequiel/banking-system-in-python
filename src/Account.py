from .History import History


class Account:
    def __init__(self, number: int, customer) -> None:
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._customer = customer
        self._history = History()

    @classmethod
    def new_account(cls, number: int, customer):
        return cls(number, customer)
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @property
    def number(self) -> int:
        return self._number
    
    @property
    def agency(self) -> str:
        return self._agency
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def history(self):
        return self._history
    
    def withdraw(self, value: float) -> bool:

        if value > 0:
            self._balance -= value
            return True
        
        elif self._balance < value:
            print("Insufficient funds")

        else:
            print("Invalid value")

        return False

    def deposit(self, value: float) -> bool:
        if value > 0:
            self._balance += value
            return True
        else:
            print("Invalid value")
            return False

    def extract(self) -> None:
        pass