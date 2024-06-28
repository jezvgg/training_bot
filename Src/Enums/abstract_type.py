from abc import ABC


class abstract_type(ABC):
    __name = ''

    def __init__(self, name: str) -> None:
        self.__name = name

    def __hash__(self):
        return hash(self.__name)

    @property
    def name(self):
        return self.__name
