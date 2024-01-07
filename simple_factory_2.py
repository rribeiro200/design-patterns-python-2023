from abc import ABC, abstractmethod

# Produto / Contrato - Abstrato
class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


# Concretização do produto/contrato - Implementação
class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente... ')


# Concretização do produto/contrato - Implementação
class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente... ')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente... ')

class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo está buscando o cliente... ')


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    # Método de fabricação (do carro no caso...)
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        match tipo:
            case 'luxo':
                return CarroLuxo()
            case 'popular':
                return CarroPopular()
            case 'moto':
                return MotoPopular()
            case 'moto_luxo':
                return MotoLuxo()
            case _:
                assert 0, 'Veiculo não existe'
    
    def buscar_cliente(self):
        self.carro.buscar_cliente()

if __name__ == '__main__':
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto', 'moto_luxo']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis)) # Cliente pede para factory o objeto
        carro.buscar_cliente