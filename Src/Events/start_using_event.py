from Src.Events.event import event
from aiogram import types
from Src.Models import User, Message
from Src.dialogue_manager import dialogue_manager
from DB.Tables import SubscribeInfo
from DB.DBInterface import DBInterface
from Src.settings import settings
from datetime import datetime
from Src.Models import Keyboard


class start_using_event(event):
    '''
    Показательный ивент для примера.
    Выводит в консоль пользователя и сообщение.
    '''

    _db: DBInterface
    __settings:settings



    def __init__(self, db: DBInterface):
        self._db = db
        self.__settings=settings.from_json()

    def activate(self, user: User, message: types.Message) -> Message:
        subscribes = self._db._get_ones(SubscribeInfo, user.id)
        print(user.current_message.keyboard.data)
        user.current_message.keyboard.data=[user.current_message.keyboard.data[self.__get_num(subscribes)]]
        return user.current_message
        

        
    
    def __get_num(self,subscribe):
        print(subscribe)
        if len(subscribe)==0:
            return 1
        elif subscribe[-1].subscribe_end > datetime.now():
            return 2
        else:
            return 0
    