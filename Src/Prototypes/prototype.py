from abc import ABC
from random import sample


class prototype(ABC):
    '''абстрактный проттотип'''
    _data:list


    def __init__(self, data: list):
        '''
        Args:
            data - list определённого типа
        '''
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
        '''
        список данных в прототипе
        '''
        return self._data