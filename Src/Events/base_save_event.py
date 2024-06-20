from Src.Events import event
from DB.DBInterface import DBInterface
from Src.Models import User, Message
from aiogram import types
from typing import Callable




class field:
    message: Message
    type: Callable

    def __init__(self, message: Message, type: Callable = lambda x: x):
        self.message = message
        self.type = type




class base_save_event(event):
    '''
    Абстрактный Ивент проведения опрос и сохранения данных пользователя
    '''
    _db: DBInterface
    _table_class: type
    _questions: dict[str: field]
    __map: dict[str: str]
    _start_message: int


    def __init__(self, db: DBInterface):
        self._db = db
        self._start_message = None


    def _start(self, user: User, message: types.Message) -> Message:
        if self._start_message is None:
            self._start_message = user.current_message.id
        table = self._table_class(user.id)
        self._db._add(table)
        return list(self._questions.values())[0].message


    def _next(self, user: User, message: types.Message) -> Message:
        info = self._db._get_one(self._table_class, user.id)

        varnames = list(self._questions.keys())
        for i,varname in enumerate(varnames):
            if varname.startswith('_') or getattr(info, varname) is not None: continue
            print(varname)
            setattr(info, varname, self._questions[varname].type(message.text))
            self._db._update()

            if i+1 >= len(varnames):
                return self._finish(user, message)

            next_message = self._questions[varnames[i+1]]
            return next_message.message


    def _finish(self, user: User, message: types.Message) -> Message:
        return user.current_message


    def _activate(self, user: User, message: types.Message) -> Message:
        if not self._db._get_ones(self._table_class, user.id):
            return self._start(user, message)

        return self._next(user, message)


    @property
    def table_class(self):
        return self._table_class


    @table_class.setter
    def table_class(self, set: type):
        self.__map = {getattr(value, 'name'):key for key, value in vars(set).items() if hasattr(value, 'name')}
        self._table_class = set


    @property
    def questions(self):
        return self._questions


    @questions.setter
    def questions(self, value: dict[str: Message]):
        self._questions = {self.__map[item[0]]:item[1] for item in value.items()}
