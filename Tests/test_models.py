import unittest
from Src.Models import *
from Src.settings import settings
from datetime import datetime


class test_models(unittest.TestCase):
    '''
    Проверка создания моделей, их функций (если таковые есть) и фабричных методов.
    '''

    def test_settings_model(self):
        
        sets = settings('test', '1111', '127.0.0.1', '5432', 'test', 'url', 'token', '', '')

        assert sets is not None


    def test_message_model(self):
        
        msg = Message(1, 'Первое тестовое сообщение', 2)
        assert msg.id != None

        error_msg = Message.error_message()
        assert error_msg.id == 0


    def test_user_model(self):

        msg = Message(1, 'Первое тестовое сообщение', 2)
        usr = User(True, False, '', msg, datetime.now(), datetime.now(), 1)

        assert usr.current_message.id is not None
        assert usr.id is not None


    def test_command_model(self):

        msg = Message(1, 'Первое тестовое сообщение', 2)
        cmd = Command('', msg, 'start')

        assert cmd is not None
        assert cmd.name == '/start'


    def test_keyboard_model(self):

        kbd = Keyboard(0, [{'Yes':0, 'No':1}])

        assert kbd is not None
        assert kbd.build_markup() is not None