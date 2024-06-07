from Src.Models.AbstractModel import AbstractModel


class Keyboard(AbstractModel):
    __id: int
    __data: list[list[int|str]]


    def __init__(self, id:int, data: list[list[int|str]]) -> None:
        self.__data: list[list[int|str]] = data
        self.__id = id


    @property
    def id(self) -> int:
        return self.__id


    @property
    def data(self) -> list[list[int|str]]:
        return self.__data