


class Keyboard:
    __data: list[list[int|str]]


    def __init__(self, data: list[list[int|str]]) -> None:
        self.__data: list[list[int|str]] = data
        pass


    @property
    def data(self) -> list[list[int|str]]:
        return self.__data