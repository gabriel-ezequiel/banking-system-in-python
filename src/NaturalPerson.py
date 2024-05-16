from .Customer import Customer


class NaturalPerson(Customer):
    def __init__(self, CPF: str, name: str, date_of_birth: str, adress: str) -> None:
        super().__init__(adress)
        self.CPF = CPF
        self.name = name
        self.date_of_birth = date_of_birth