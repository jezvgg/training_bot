from abc import ABC
from random import sample


class prototype(ABC):
    _data:list


    def __init__(self, data: list):
        self._data = data


    def sample(self):
        '''
        Вернуть случайный элемент прототипа
        '''
        return self.samples(1)[0]


    def samples(self, amount: int = 1):
        '''
        Возвращает n разных элементов их прототипа
        '''
        return sample(self._data, amount)


    @property
    def data(self):
        return self._data