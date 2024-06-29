from Src.Events import *
from DB.DBInterface import DBInterface
from Src.dialogue_manager import dialogue_manager


class event_handler:
    '''
    Фабрика на ключевых словах, возращает класс ивента
    '''
    __map: dict[str, event]


    def __init__(self, db: DBInterface):
        self.__map = {'show': show_event(),
                      'save_user_info': save_user_event(db),
                      'training_data':save_training_event(db),
                      'diet_save_event':diet_save_event(db),
                      'diet_get_event':diet_get_event(db)}


    def get_event(self, eventname: str):
        '''
        Получить ивент

        Args:
            eventname - название ивента
        '''
        return self.__map[eventname]


    @property
    def events(self):
        return self.__map