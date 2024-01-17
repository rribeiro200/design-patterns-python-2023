from collections.abc import Iterator, Iterable
from typing import List, Any

## ITERADOR CONCRETO ##
class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0
    
    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration
        

## AGREGADOR CONCRETO ###
class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
    
    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self):
        print('Itens dentro do dunder ITER', self._items)
        return MyIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'
    

if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Rafael')
    mylist.add('Pedro')
    mylist.add('Julia')
    mylist.add('Maria')

    print(mylist)

    for value in mylist:
        print(value)