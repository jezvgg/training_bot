from Src.Events import base_save_event
from DB.DBInterface import DBInterface
from DB.Tables import UserInfoTable


class save_user_event(base_save_event):
    

    def __init__(self, db: DBInterface):
        super().__init__(db)
        self._table_class = UserInfoTable
        self._questions = {UserInfoTable.gender.name: 'Отлично, мы начинаем опрос. \nПодскажите, какого вы пола?',
                           UserInfoTable.username.name: 'И как я могу к вам обращаться?'}
        
