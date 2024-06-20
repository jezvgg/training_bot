from Src.Events.base_save_event import base_save_event, field
from DB.DBInterface import DBInterface
from DB.Tables import UserInfoTable
from Src.Models import Message, Keyboard, User
from aiogram import types


class save_user_event(base_save_event):
    

    def __init__(self, db: DBInterface):
        super().__init__(db)
        self.table_class = UserInfoTable
        self.questions = self.make_questions()

    
    def _finish(self, user: User, message: types.Message) -> Message:
        info = self._db._get_one(self._table_class, user.id)

        text = f'''Получается вот так:\n
        {info.username} {info.age} лет, из {info.city}. Вес {info.weight} при росте {info.height}?
        '''

        finish_message = Message(0, text, 0,
            keyboard=Keyboard(0, [{'Да':user.current_message.next_message_id, 'Нет':self._start_message}]))
        return finish_message


    def activate(self, user: User, message: types.Message) -> Message:
        message_ = self._activate(user, message)

        if message_ is None:
            self._db._delete(self._db._get_one(UserInfoTable, user.id))
            message_ = self._activate(user, message)
        print(message_)

        return message_
        

    def make_questions(self):
        gender_questions = Message(0, 'Начинаем опрос.\nКакого вы пола?', 0, 
                            keyboard=Keyboard(0, [{'Мужской':2, 'Женский':3}]))
        return {
            UserInfoTable.username.name: field(Message(0, 'Как я могу к вам обращаться?', 0)),
            UserInfoTable.age.name: field(Message(0, 'А сколько вам лет?', 0), int),
            UserInfoTable.city.name: field(Message(0, 'А из какого вы города?', 0)),
            UserInfoTable.weight.name: field(Message(0, 'Какой у вас текущий вес?', 0), int),
            UserInfoTable.height.name: field(Message(0, 'При каком росте?', 0), int)
        }
        
