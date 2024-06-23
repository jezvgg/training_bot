import unittest
from Src.Models import *
from Src.Services.telegram_service import telegram_service
from Src.commands_manager import command_manager
from Src.dialogue_manager import dialogue_manager
from DB.DBTest import DBTest
from collections import namedtuple


class test_services(unittest.TestCase):
    '''
    Тестирование сервисов
    '''
    def test_telegram_service(self):

        dmanager = dialogue_manager([Message.error_message()])
        cmanager = command_manager([])
        db = DBTest(User(True, False, '', Message.error_message(), False, 0))

        service = telegram_service(dmanager, cmanager, db)

        answer = service.create_answer(Message.error_message())

        assert answer is not None
        assert answer['text'] != ''


    def test_telegram_user(self):

        dmanager = dialogue_manager([Message.error_message()])
        cmanager = command_manager([])
        db = DBTest(User(True, False, '', Message.error_message(), False, 0))

        service = telegram_service(dmanager, cmanager, db)

        user = service.get_user(1)

        assert user is not None

        user2 = service.get_user(1)

        assert user2 is not None
        assert user == user2


    def test_handle_message(self):
        dmanager = dialogue_manager([Message.error_message()])
        cmanager = command_manager([])
        db = DBTest(User(True, False, '', Message.error_message(), False, 0))
        service = telegram_service(dmanager, cmanager, db)

        message = namedtuple('message', ['text'])
        mes = message('some text')
        user = User(True, False, '', Message.error_message(), False, 0)

        output = service.handle_message(user, mes)

        assert output is not None
        assert output.id == Message.error_message().id


    def test_handle_command(self):
        dmanager = dialogue_manager([Message.error_message()])
        cmanager = command_manager([Command('',Message.error_message(),'start')])
        db = DBTest(User(True, False, '', Message.error_message(), False, 0))
        service = telegram_service(dmanager, cmanager, db)

        message = namedtuple('message', ['text'])
        mes = message('/start')
        user = User(True, False, '', Message.error_message(), False, 0)

        output = service.handle_command(user, mes)

        assert output is not None
        assert output.id == Message.error_message().id

    def test_handle_callback(self):
        dmanager = dialogue_manager([Message.error_message()])
        cmanager = command_manager([])
        db = DBTest(User(True, False, '', Message.error_message(), False, 0))
        service = telegram_service(dmanager, cmanager, db)

        callback = namedtuple('callback', ['data', 'message'])
        message = namedtuple('message', ['text'])
        call = callback('0', message('xyi'))
        user = User(True, False, '', Message.error_message(), False, 0)

        output = service.handle_callback(user, call)

        assert output is not None
        assert output.id == Message.error_message().id
        
        