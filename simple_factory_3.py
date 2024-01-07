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



# Neste caso de filiais, eu abstraio a empresa
# Creator
class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    # Factory method - Abstrato
    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass
    
    def buscar_cliente(self):
        self.carro.buscar_cliente()


# Concret Creator - Classe que implementa o Factory Method
class ZonaNorteVeiculoFactory(VeiculoFactory):
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


# Concret Creator - Classe que implementa o Factory Method
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        match tipo:
            case 'popular':
                return CarroPopular()
            case _:
                assert 0, 'Não possuo este veiculo na zona sul'



if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte)) # Cliente pede para factory o objeto        
        carro.buscar_cliente()
    
    print()
    print()

    print('ZONA SUL')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul)) # Cliente pede para factory o objeto
        carro2.buscar_cliente()