from __future__ import annotations
from abc import ABC, abstractmethod


""" CONTEXT """
class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('Estado atual: ', self.state)
        self.state.pending()

    def approve(self) -> None:
        print('Estado atual: ', self.state)
        self.state.approve()

    def reject(self) -> None:
        print('Estado atual: ', self.state)
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self):
        return self.__class__.__name__


# Estado da Order
class PaymentPending(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print('Pagamento já pendente, não posso fazer nada.')
    
    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado')

    def reject(self) -> None: 
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')


# Estado da Order
class PaymentApproved(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None: 
        self.order.state = PaymentPending(self.order)
    
    def approve(self) -> None:
        print('Pagamento já aprovado, não posso fazer nada')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)


# Estado da Order
class PaymentRejected(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print('Pagamento recusado. Não vou mover para pendente')

    def approve(self) -> None:
        print('Pagamento recusado. Não vou mover para aprovado')

    def reject(self) -> None:
        print('Pagamento recusado. Não vou recusar novamente')


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()