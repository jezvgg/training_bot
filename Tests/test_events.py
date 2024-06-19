import unittest
from Src.Events import show_event
from Src.Models import User, Message
from collections import namedtuple


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
        assert result == 'done'