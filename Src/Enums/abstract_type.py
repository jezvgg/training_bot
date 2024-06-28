from abc import ABC


class abstract_type(ABC):
    __name = ''

    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name
