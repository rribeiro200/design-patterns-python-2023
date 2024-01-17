from __future__ import annotations
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self):
        return self.__str__()


class Order(StringReprMixin):
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)
    


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass



class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)
    


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)
    


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value
    


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()

    order1 = Order(1000, twenty_percent)
    order2 = Order(1000, fifty_percent)

    print(order1)
    print(order2)