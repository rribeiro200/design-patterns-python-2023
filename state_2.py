from __future__ import annotations
from abc import ABC, abstractmethod

class Sound:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)  # type: ignore
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        print(f'Mudando para mode {self.mode}')
        self.playing = 0
        self.mode = mode

    def press_next(self) -> None:
        print(self)
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        self.mode.press_prev()

    def __str__(self) -> str:
        return str(self.playing)


## ESTADO ABSTRATO ##
class PlayMode(ABC):
    def __init__(self, sound: Sound):
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None: pass

    @abstractmethod
    def press_prev(self) -> None: pass


## ESTADO CONCRETO ##
class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000

    def press_prev(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0


## ESTADO CONCRETO ##
class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1

    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing > 0 else 0


if __name__ == '__main__':
    sound = Sound()
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_next()

    print()
    sound.change_mode(MusicMode(sound))
    sound.press_next()
    sound.press_next()
    sound.press_next()