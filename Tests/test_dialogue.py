import unittest
from Src.Models import *
from Src.Dialogue_manager import Dialogue_manager


class test_dialogue(unittest.TestCase):
    '''
    Тестирование способности бота введения диалога (Dialogue_manager)
    '''
    def test_dialogue_messages(self):
        msg1 = Message(1, 'Первое сообщение', 2)
        msg2 = Message(2, 'Второе сообщение', 4)
        msg3 = Message(3, 'Последнее сообщение', 4)
        msg4 = Message(4, 'Рекурсионное сообщение', 3)

        messages = {1: msg1,
                    2: msg2,
                    3: msg3,
                    4: msg4}

        manager = Dialogue_manager(messages)

        first_msg = manager.get_start()
        assert first_msg == msg1
        print(first_msg.text)
        second_msg = manager.get_next(first_msg)
        assert second_msg == msg2
        print(second_msg.text)
        thrid_msg = manager.get_next(second_msg)
        assert thrid_msg == msg4
        print(thrid_msg.text)
        fourth_msg = manager.get_next(thrid_msg)
        assert fourth_msg == msg3
        print(fourth_msg.text)
        to_recursion_msg = manager.get_next(fourth_msg)
        assert to_recursion_msg == msg4
        print(to_recursion_msg.text)

        