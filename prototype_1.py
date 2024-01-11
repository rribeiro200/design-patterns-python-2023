from __future__ import annotations
from typing import List
from copy import deepcopy

class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()
    

class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)
    
    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    rafael = Person('Rafael', 'Ribeiro')
    endereco_rafael = Address('Américo de Paiva', '64')
    rafael.add_address(endereco_rafael)

    esposa_rafael = rafael.clone()
    esposa_rafael.firstname = 'Julia'

    print(rafael)
    print(esposa_rafael)