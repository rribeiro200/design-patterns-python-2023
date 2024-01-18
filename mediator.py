from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Colleague(ABC):
    def __init__(self):
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None: 
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None: pass


# Concrete Mediator
class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []
    

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues
    

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    
    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return  # Não quero fazer nada
        
        print(f'{colleague.name} disse: {msg}')

    
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return  # Não quero fazer nada
        
        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return 
        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    # Instanciando o mediador
    chat = Chatroom()

    # Definindo as pessoas que usaram o mediador para se comunicar
    rafa = Person('Rafa', chat)
    diandra = Person('Diandra', chat)
    pedro = Person('Pedro', chat)

    # Adicionando um colega no chat (mediador)
    # Temos um mediador(sala de bate papo) e usuários(colegas)
    chat.add(rafa)
    chat.add(diandra)
    chat.add(pedro)

    # Transmitindo mensagens entre os brothers
    rafa.broadcast('Olá pessoas!')

    rafa.send_direct('Diandra', 'Oi Diandra! Tudo bem?')