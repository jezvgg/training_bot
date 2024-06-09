import unittest
from Src.Models import *


class test_models(unittest.TestCase):
    '''
    Проверка создания моделей, их функций (если таковые есть) и фабричных методов.
    '''

    def test_message_model(self):
        
        msg = Message(1, 'Первое тестовое сообщение', 2)
        assert msg.id != None

        error_msg = Message.error_message()
        assert error_msg.id == 0


    def test_user_model(self):

        msg = Message(1, 'Первое тестовое сообщение', 2)
        usr = User(True, True, 'Username', msg, False, 113133313)

        assert usr.current_message.id is not None
        assert usr.id is not None