from Src.Events import base_save_event
from DB.DBInterface import DBInterface
from DB.Tables import UserInfoTable
from DB.Tables import DietInfoTable
from Src.Models import Message, Keyboard, User
from Src.Events import diet_get_event
from aiogram import types
from requests import post




class diet_save_event(base_save_event):
    '''
    Опрос для создания диеты
    '''
    __get_diet: diet_get_event



    def __init__(self, db: DBInterface):
        super().__init__(db)
        self.__get_diet=diet_get_event(db)
        self.table_class = DietInfoTable
        self.types = {
            DietInfoTable.product.name: str,
            DietInfoTable.diet_goal.name: str,
            DietInfoTable.count_trainings.name: str

            
        }
        

    
    def _finish(self, user: User, message: types.Message) -> Message:
        return self.__get_diet.activate(user,message)


    def activate(self, user: User, message: types.Message) -> Message:
        message_ = super().activate(user, message)

        return message_
        
    
    
