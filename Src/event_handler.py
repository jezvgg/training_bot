from Src.Events import *


class event_handler:
    '''
    Фабрика на ключевых словах, возращает класс ивента
    '''
    __map: dict[str, event] = {'show': show_event}

    @classmethod
    def get_event(cls, eventname: str):
        '''
        Получить ивент

        Args:
            eventname - название ивента
        '''
        return cls.__map[eventname]