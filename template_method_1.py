from abc import ABC, abstractmethod

""" CLASSE ABSTRATA """
class Pizza(ABC):
    def prepare(self) -> None:
        """ TEMPLATE METHOD """
        self.hook_before_add_ingredtients()  # Hook
        self.add_ingrentients()  # Abstract
        self.hook_after_add_ingredtients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concreto
        self.serve()  # Concreto

    def hook_before_add_ingredtients(self) -> None: pass 
    def hook_after_add_ingredtients(self) -> None: pass 

    def cut(self):
        print(f'{self.__class__.__name__}: Cortando pizza.')

    def serve(self):
        print(f'{self.__class__.__name__}: Servindo pizza.')

    @abstractmethod
    def add_ingrentients(self): pass

    @abstractmethod
    def cook(self): pass


class AModa(Pizza):
    def add_ingrentients(self) -> None:
        print(f'AModa - adicionando ingredientes: presunto, queijo, goiabada')

    def cook(self) -> None: 
        print(f'AModa - cozinhando por 45min no forno a lenha')


class Veg(Pizza):
    def hook_before_add_ingredtients(self) -> None:
        print(f'{__class__.__name__} - Lavando ingredientes')

    def add_ingrentients(self):
        print(f'{__class__.__name__} - adicionando ingredientes: presunto, queijo, goiabada')

    def cook(self) -> None:
        print(f'{__class__.__name__} - cozinhando por 5min no forno comum')


if __name__ == '__main__':
    a_moda = AModa()
    a_moda.prepare()

    print()

    veg = Veg()
    veg.prepare()