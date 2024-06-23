from Src.Models import Keyboard, AbstractModel
from dataclasses import dataclass,field

@dataclass
class Message(AbstractModel):
    '''
    Модель сообщения.

    Фабричные методы:
        error_message: Сообщение об ошибке.
    '''
    __id: int
    __text: str
    __next_message_id: int
    __event_name: str=field(default=None)
    __keyboard: Keyboard=field(default=None)



    @staticmethod
    def error_message():
        '''
        Сообщение об ошибке.
        '''
        return Message(0, 'Если вы видите это сообщение, то произошла ошибка. Напишите об этом администрации.', 0)



    @property
    def id(self) -> int:
        return self.__id


    @property
    def text(self) -> str:
        return self.__text


    @text.setter
    def text(self, value: str) -> None:
        self.__text = value
        

    @property
    def keyboard(self) -> Keyboard:
        return self.__keyboard


    @property
    def event_name(self) -> str:
        return self.__event_name


    @property
    def next_message_id(self) -> int:
        return self.__next_message_id