from Src.Events import *
from DB.DBInterface import DBInterface


class event_handler:
    '''
    Фабрика на ключевых словах, возращает класс ивента
    '''
    __map: dict[str, event]


    def __init__(self, db: DBInterface):
        self.__map = {'show': show_event()}


    def get_event(self, eventname: str):
        '''
        Получить ивент

        Args:
            eventname - название ивента
        '''
        return self.__map[eventname]