import unittest
from Src.Models import *
from Src.Services.telegram_service import telegram_service
from Src.commands_manager import command_manager
from Src.dialogue_manager import dialogue_manager



class test_services(unittest.TestCase):
    '''
    Тестирование сервисов
    '''
    def test_telegram_service(self):
        
        user = User(True, False, '', Message.error_message(), False, 0)

        answer = telegram_service.create_answer(user)

        assert answer is not None
        assert answer['text'] != ''
        