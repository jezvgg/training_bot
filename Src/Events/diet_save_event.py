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
        print("start")

        return self.__get_diet.activate(user,message)


    def activate(self, user: User, message: types.Message) -> Message:

        info_diet = self._db._get_ones(DietInfoTable, user.id)
        if len(info_diet)==0:
            return self._start(user, message)

        info_diet = sorted(info_diet, key=lambda x: x.subscribe_id)[-1]

        if not(info_diet.diet is  None):
            return self._start(user, message)
        

        return self._next(user, message)
    
    def _next(self, user: User, message: types.Message) -> Message | None:
        '''
        Метод, вызываемый для перехода не следующий вопрос,
        он так же и сохраняет данные.
        '''
        # info - данные которые мы сохраняем
        info = self._db._get_ones(self._table_class, user.id)
        info= sorted(info, key=lambda x: x.subscribe_id)[-1]

        varnames = list(self._types.keys())
        for varname in varnames:
            # Если в поле есть данные, то не заполняем его
            if getattr(info, varname) is not None: continue
            
            # Данные для заполнения, либо текст сообщения либо текст нажатой кнопки
            value = message.text
            if message.reply_markup:
                id = user.current_message.id
                keyboard = message.reply_markup.inline_keyboard
                value = [button.text for row in keyboard for button in row if button.callback_data==str(id)][0]

            setattr(info, varname, self._types[varname](value))
            self._db._update()

            if varnames[-1] == varname:
                return self._finish(user, message)

            return user.current_message
        
    
    
