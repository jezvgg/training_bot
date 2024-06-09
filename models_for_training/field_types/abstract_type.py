from abc import ABC


class abstract_type(ABC):
    __name=''


    def __init__(self,name:str) -> None:
        self.__name=name