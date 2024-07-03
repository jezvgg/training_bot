from Src.Models import Message, AbstractModel
from datetime import datetime


class Subscribe(AbstractModel):
    '''
    Модель пользователя
    '''
    __telegram_id: int
    __subscribe_start: datetime
    __subscribe_end: datetime
    __count_subskribe_day: int
    __subscribe_level: int
    


    def __init__(self, id: int,  subscribe_start: datetime, subscribe_end: datetime,  count_subskribe_day: int, subscribe_level: int = 1) -> None:
        '''
        Модель пользователя

        Args:
            subscribe_id - уникальный номер записи об оплате подписки
            telegram_id - уникальный номер пользователя, из телеграма
            subscribe_start - дата начала подписки 
            subscribe_end - дата конца подписки
            count_subscribe_day - кличество дней которые польщователь был с подписккой 
            subscribe_leverel - уровень подписки             
        '''
        self.__subscribe_level = subscribe_level
        self.__telegram_id: int = id
        self.__subscribe_start: datetime = subscribe_start
        self.__subscribe_end: datetime = subscribe_end
        self.__count_subskribe_day: int = count_subskribe_day



    @property
    def id(self) -> int:
        return self.__telegram_id
    

    @property
    def subscribe_start(self) -> datetime:
        return self.__subscribe_start
    

    @property
    def subscribe_end(self) -> datetime:
        return self.__subscribe_end
    

    @property
    def count_subskribe_day(self) -> int:
        return self.__count_subskribe_day
    

    @property
    def subscribe_level(self) -> int:
        return self.__subscribe_level


    


    

