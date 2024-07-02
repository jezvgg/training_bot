from Src.Events.base_save_event import base_save_event
from DB.DBInterface import DBInterface
from DB.Tables import UserInfoTable
from Src.Models import Message, Keyboard, User
from aiogram import types


class save_user_event(base_save_event):
    '''
    Первоначальный опрос пользователя по основным данным.
    '''

    def __init__(self, db: DBInterface):
        super().__init__(db)
        self.table_class = UserInfoTable
        self.types = {
            UserInfoTable.gender.name: lambda x: {'Мужской':True, 'Женский':False}[x],
            UserInfoTable.username.name: str,
            UserInfoTable.age.name: int,
            UserInfoTable.city.name: str,
            UserInfoTable.weight.name: int,
            UserInfoTable.height.name: int
        }

    
    def _finish(self, user: User, message: types.Message) -> Message:
        # Вот тут реализация логики на основе введёных до этого данных
        # Для Мишы и Дани!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
        info = self._db._get_one(self._table_class, user.id)

        text = user.current_message.text.format(
            name=info.username, age=info.age, city=info.city, weight=info.weight, height=info.height
        )

        finish_message = Message(0, text, 0,'',Keyboard(0, [{'Да':user.current_message.next_message_id, 'Нет':self._start_message}]))
        return finish_message


    def activate(self, user: User, message: types.Message) -> Message:
        '''активация ивента'''
        message_ = super().activate(user, message)

        if message_ is None:
            self._db._delete(self._db._get_one(UserInfoTable, user.id))
            message_ = super().activate(user, message)

        return message_
        
        
