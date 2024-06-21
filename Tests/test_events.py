import unittest
from Src.Events import *
from Src.Models import User, Message
from DB.Tables import UserInfoTable
from collections import namedtuple
from DB.DBTest import DBTest


class test_events(unittest.TestCase):
    '''
    Тестирование ивентов
    '''
    def test_show(self):
        user = User(True, False, '', Message.error_message(), False, 0)
        # Вместо сообщения телеграмма
        message = namedtuple('message', ['text'])
        mes = message('some text')
        result = show_event().activate(user, mes)

        assert result is not None
        assert result.text == Message.error_message().text

    def test_save_user_start(self):
        db = DBTest(UserInfoTable(0, False, 'lox', 18, 'Irkutsk', 71, 171))
        user = User(True, False, '', Message.error_message(), False, 0)
        message = namedtuple('message', ['text'])
        mes = message('some text')

        event = save_user_event(db)

        lenght1 = len(db.get(UserInfoTable))
        output = event._start(user, mes)
        lenght2 = len(db.get(UserInfoTable))

        assert output is not None
        assert output.id == Message.error_message().id
        assert lenght1 < lenght2


    def test_save_user_next(self):
        db = DBTest(User(True, False, '', Message.error_message(), False, 0), UserInfoTable(2, False, 'lox', 18, 'Irkutsk', 71, 171))
        user = User(True, False, '', Message.error_message(), False, 0)
        message = namedtuple('message', ['text', 'reply_markup'])
        mes = message('Мужской', None)

        event = save_user_event(db)

        event._start(user, mes)
        output = event._next(user, mes)

        assert output is not None
        assert output.id == Message.error_message().id


    def test_save_user_finish(self):
        db = DBTest(User(True, False, '', Message.error_message(), False, 0), UserInfoTable(2, False, 'lox', 18, 'Irkutsk', 71, 171))
        user = User(True, False, '', Message.error_message(), False, 0)
        message = namedtuple('message', ['text'])
        mes = message('some text')

        event = save_user_event(db)

        event._start(user, mes)
        output = event._finish(user, mes)

        assert output is not None
        assert output.id == Message.error_message().id
        assert output.keyboard is not None

    def test_save_user_activate(self):
        db = DBTest(User(True, False, '', Message.error_message(), False, 0), UserInfoTable(2, False, 'lox', 18, 'Irkutsk', 71, 171))
        user = User(True, False, '', Message.error_message(), False, 0)
        message = namedtuple('message', ['text'])
        mes = message('some text')

        event = save_user_event(db)

        output = event.activate(user, mes)

        assert output is not None
        assert output.id == Message.error_message().id