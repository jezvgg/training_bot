from Src.Models.Keyboard import Keyboard


class Message:
    '''
    Модель сообщения.

    Фабричные методы:
        error_message: Сообщение об ошибке.
    '''
    __id: int
    __text: str
    __keyboard: Keyboard
    __event_name: str
    __next_message_id: int


    @staticmethod
    def error_message():
        '''
        Сообщение об ошибке.
        '''
        return Message(0, 'Если вы видите это сообщение, то произошла ошибка. Напишите об этом администрации.', 0)


    def __init__(self, id: int, text: str, next_message_id: int, event_name: str = '', keyboard: Keyboard = None) -> None:
        '''
        Модель сообщения.

        Args:
            id - айди сообщения.
            text - текст сообщения.
            keyboard - объект класса Keyboard, для создания reply_keyboard в боте.
            event_name - ключ евента для его вызова.
            next_message_id - айди сообщения, которые будет после этого, если пользователь не перейдёт на другое другим методом.
        '''
        self.__id: int = id
        self.__text: str = text
        self.__keyboard: Keyboard = keyboard
        self.__event_name: str = event_name
        self.__next_message_id: int = next_message_id


    @property
    def id(self) -> int:
        return self.__id


    @property
    def text(self) -> str:
        return self.__text


    @property
    def keyboard(self) -> Keyboard:
        return self.__keyboard


    @property
    def event_name(self) -> str:
        return self.__event_name


    @property
    def next_message_id(self) -> int:
        return self.__next_message_id