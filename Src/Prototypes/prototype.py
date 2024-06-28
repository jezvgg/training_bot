from abc import ABC
from random import sample


class prototype(ABC):
    __is_error:bool=False
    __data:list=[]


    def __init__(self) -> None:
        super().__init__()
    

    def sample(self,amount:int=1):
        return sample(self.__data,amount)