class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {
        'Leite': 10,
        'y': 20,
    }

    def __init__(self):
        self.__dict__ = self._state



if __name__ == '__main__':
    m1 = MonoStateSimple()
    sr1 = StringReprMixin()
    print(m1)
    print(sr1)