from Src.Models import Message, AbstractModel

from Src.Models import Message, AbstractModel



class User(AbstractModel):

    '''
    Модель пользователя
    '''
    __telegram_id: int
    __current_message: Message
    __username: str
    __is_accepted: bool
    __is_use: bool


    def __init__(self, is_use: bool, is_accepted: bool, username: str, \
    current_message: Message, id: int) -> None:
        '''
        Модель пользователя

        Args:
            telegram_id - уникальный номер пользователя, из телеграма
            current_message - сообщение на котором остановился пользователь
            username - имя пользователя
            is_accepted - принял ли условия соглашения пользователь
            is_use - если false значит забанен
        '''
        self.__telegram_id: int = id
        self.__current_message: Message = current_message
        self.__username: str = username
        self.__is_accepted: bool = is_accepted
        self.__is_use: bool = is_use


    @property
    def id(self) -> int:
        '''уникальный номер пользователя, из телеграма'''
        return self.__telegram_id


    @property
    def current_message(self) -> Message:
        '''сообщение на котором остановился пользователь'''
        return self.__current_message


    @current_message.setter
    def current_message(self, value : Message) -> None:
        self.__current_message = value


    @property
    def username(self) -> str:
        '''имя пользователя'''
        return self.__username


    @username.setter
    def username(self, value : str) -> None:
        self.__username = value


    @property
    def is_accepted(self) -> bool:
        '''принял ли условия соглашения пользователь'''
        return self.__is_accepted


    @is_accepted.setter
    def is_accepted(self, value : bool) -> None:
        self.__is_accepted = value


    @property
    def is_use(self) -> bool:
        '''если false значит забанен'''
        return self.__is_use


    @is_use.setter
    def is_use(self, value : bool) -> None:
        self.__is_use = value