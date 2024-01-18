from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


##### USA PARA SALVAR O ESTADO DO ORIGINATOR #####
class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        object.__setattr__(self, '_state', state)

    def get_state(self) -> Dict:
        return self._state
    
    # Tornando a classe IMUTÁVEL
    def __setattr__(self, name, value):
        raise AttributeError('Sorry, I am immutable')
    
    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


##### O QUE QUEREMOS SALVAR O ESTADO #####
class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))
    
    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


##### ARMAZENAR LEMBRANÇAS #####
class CareTaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None: 
        self._mementos.append(self._originator.save_state())
        print(self._mementos)

    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    img = ImageEditor('FOTO_1.jpg', 111, 111)
    caretaker = CareTaker(img)

    caretaker.backup()
    
    img.name = 'Foto_2.jpG'
    img.width = 222
    img.height = 222
    caretaker.backup()
