from Src.Models.AbstractModel import AbstractModel
from dataclasses import dataclass,field

@dataclass
class Keyboard(AbstractModel):
    __id: int
    __data: list[list[int|str]]=field(default_factory=list[list[int|str]])




    @property
    def id(self) -> int:
        return self.__id


    @property
    def data(self) -> list[list[int|str]]:
        return self.__data