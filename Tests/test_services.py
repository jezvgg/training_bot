import unittest
from Src.Models import *
from Src.Services.telegram_service import telegram_service
from Src.commands_manager import command_manager
from Src.dialogue_manager import dialogue_manager
from DB.DBTest import DBTest


class test_services(unittest.TestCase):
    '''
    Тестирование сервисов
    '''
    def test_telegram_service(self):
        
        user = User(True, False, '', Message.error_message(), False, 0)

        answer = telegram_service.create_answer(user)

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
        