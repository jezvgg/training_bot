from Src.Models import Message, AbstractModel, Period
from dataclasses import dataclass,field

from datetime import datetime

@dataclass
class User(AbstractModel):

    '''
    Модель пользователя
    '''
    __is_use: bool
    __is_accepted: bool
    __username: str
    __current_message: Message
    __subcribe: Period
    __telegram_id: int








    @property
    def id(self) -> int:
        return self.__telegram_id


    @property
    def subscribe(self) -> Period:
        return self.__subscribe


    @subscribe.setter
    def subscribe(self, value : Period) -> None:
        self.__subscribe = value


    @property
    def current_message(self) -> Message:
        return self.__current_message


    @current_message.setter
    def current_message(self, value : Message) -> None:
        self.__current_message = value


    @property
    def username(self) -> str:
        return self.__username


    @username.setter
    def username(self, value : str) -> None:
        self.__username = value


    @property
    def is_accepted(self) -> bool:
        return self.__is_accepted


    @is_accepted.setter
    def is_accepted(self, value : bool) -> None:
        self.__is_accepted = value


    @property
    def is_use(self) -> bool:
        return self.__is_use


    @is_use.setter
    def is_use(self, value : bool) -> None:
        self.__is_use = value