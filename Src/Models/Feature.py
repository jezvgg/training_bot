from dataclasses import dataclass, field
from Src.Models import AbstractModel, Message


@dataclass
class Feature(AbstractModel):
    __id: int
    __message: Message = field(init=False, repr=False)
    __text: str = field(init = False)
    text: str


    @property
    def id(self) -> int:
        return self.__id


    @property
    def message(self) -> Message:
        return self.__message


    @property
    def text(self) -> str:
        return self.__text


    @text.setter
    def text(self, value : str) -> None:
        self.__message = Message(0, value, 0)
        self.__text = value