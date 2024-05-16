from abc import ABC, abstractmethod


class Transaction(ABC):
    @property
    @abstractmethod
    def value(self) -> float:
        pass

    @abstractmethod
    def record(self, account):
        pass