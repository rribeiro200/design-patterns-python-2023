from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


""" Component """
class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


""" Composite """
class Box(BoxStructure):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            print(child)
            child.print_content()
    
    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])
    
    def add(self, child: BoxStructure) -> None:
        self._children.append(child)
    
    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


""" Leaf """
class Product(BoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price
    

if __name__ == '__main__':
    # Leaf
    camiseta1 = Product('camiseta1', 49.90)
    camiseta2 = Product('camiseta2', 19.90)
    camiseta3 = Product('camiseta3', 10.90)

    # Composite
    caixa_camisetas = Box('Caixa de camisetas')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    # Leaf
    smartphone1 = Product('Iphone', 15000)
    smartphone2 = Product('Samsung', 5000)

    # Composite 
    caixa_smartphones = Box('Caixa de smartphones')
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)

    # Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())