from Src.Events import event
from DB.DBInterface import DBInterface
from Src.Models import User, Message
from aiogram import types
from typing import Callable


class base_save_event(event):
    '''
    Ивент для наследования - проведящий опрос и сохраняющий данные пользователя
    '''
    _db: DBInterface
    _table_class: type
    _types: dict[str: Callable]
    __map: dict[str: str]
    _start_message: int


    def __init__(self, db: DBInterface):
        self._db = db
        self._start_message = None


    def _start(self, user: User, message: types.Message) -> Message:
        '''
        Метод, который вызывается в начале опроса
        '''
        if self._start_message is None:
            self._start_message = user.current_message.id

        table = self._table_class(user.id)
        self._db._add(table)

        return user.current_message


    def _next(self, user: User, message: types.Message) -> Message | None:
        '''
        Метод, вызываемый для перехода не следующий вопрос,
        он так же и сохраняет данные.
        '''
        # info - данные которые мы сохраняем
        info = self._db._get_ones(self._table_class, user.id)
        info = [infotable for infotable in info if not all(map(bool, vars(infotable).values()))][0]

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

        # Вернёт None если пользователь уже заполнен


    def _finish(self, user: User, message: types.Message) -> Message:
        '''
        Метод, вызывающийся в конце опроса
        '''
        # Вот этот метод нужно переопределить МИША и ДАНИЛА
        # Пример в save_user_event.py
        return user.current_message


    def activate(self, user: User, message: types.Message) -> Message:
        '''
        Точка активации ивента
        '''
        if not self._db._get_ones(self._table_class, user.id):
            return self._start(user, message)

        return self._next(user, message)


    @property
    def table_class(self):
        '''
        Класс таблицы по которой нам нужно создавать опрос
        '''
        return self._table_class


    @table_class.setter
    def table_class(self, set: type):
        # __map - словарь который указывает, какое название таблицы соответсвует какому свойству
        self.__map = {getattr(value, 'name'):key for key, value in vars(set).items() if hasattr(value, 'name')}
        self._table_class = set


    @property
    def types(self):
        return self._types


    @types.setter
    def types(self, value: dict[str: Message]):
        # При добавлении сразу превращаем, чтоб ключами были не названия столбцов
        # а названия переменных
        self._types = {self.__map[item[0]]:item[1] for item in value.items()}
