from __future__ import annotations
from typing import List, Dict

class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrinsic address data
        self.address_number: str
        self.address_detail: str
    
    def add_address(self, address: Address) -> None:
        self._addresses.append(address)
    
    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_addresses(self.address_number, self.address_detail)
    

class Address:
    """Flyweight"""
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_addresses(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighborhood, 
            address_details, self._zip_code
        )

    
class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        string = ''.join(kwargs.values())
        return string
    
    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)
        
        try:
            print(self._addresses)
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')
            print(self._addresses)

        return address_flyweight
    

if __name__ == '__main__':
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil', 
        neighborhood=' Centro', 
        zip_code=' 000000-000'
    )

    rafa = Client('Rafa')
    rafa.address_number = '64'
    rafa.address_detail = 'Casa'
    rafa.add_address(a1)
    rafa.list_addresses()

    pedro = Client('Pedro')
    pedro.address_number = '250A'
    pedro.address_detail = 'AP 555 '
    pedro.add_address(a1)
    pedro.list_addresses()