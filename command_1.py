from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

## RECEIVER - Luz Inteligente ##
class Light():
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'
    
    def on(self) -> None:
        print(f' {self.name} no {self.room_name} está ON')
    
    def off(self) -> None:
        print(f' {self.name} no {self.room_name} está OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f' {self.name} no {self.room_name} agora é {self.color}')
    

## COMMAND - Inteface de Comando ##
class ICommand(ABC):
    # Executar comando
    @abstractmethod
    def execute(self) -> None: pass

    # Desfazer comando
    @abstractmethod
    def undo(self) -> None: pass


## CONCRETE COMMAND - Comando Concreto ##
class LightOnCommand(ICommand):
    def __init__(self, light: Light) -> None:
        self.light = light 
    
    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightChangeColor(ICommand):
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)

## INVOKER ##
class RemoteController:
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []
    
    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command
    
    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))
    
    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))
    
    def global_undo(self) -> None:
        if not self._undos:
            return None
        
        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == '__main__':
    # Cliente criando o RECEIVER
    bedroom_light = Light('Luz do quarto', 'Quarto A')
    bathroom_light = Light('Luz do banheiro', 'Banheiro A')

    # Cliente criando os COMANDOS
    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')

    # Cliente criando o INVOKER
    remote = RemoteController()
    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bathroom_light_on)
    remote.button_add_command('third_button', bedroom_light_blue)
    remote.button_add_command('fourth_button', bedroom_light_red)

    remote.button_pressed('fourth_button')
    remote.button_undo('fourth_button')

    print()
    print()
    print()
    print()
    remote.global_undo()
    remote.global_undo()