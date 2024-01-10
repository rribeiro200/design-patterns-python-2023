from typing import Dict

class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    


class AppSettings:
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'



if __name__ == '__main__':
    ...