from Src.Events.event import event
from aiogram import types
from Src.Models import User


class form_training_event(event):
    '''
    ивент для формирования программы из подготовленного текста.
    Выводит в консоль пользователя и сообщение.
    '''

    def activate(self, user: User, message: types.Message) -> str:
        print(user, message.text)
        return 'done'