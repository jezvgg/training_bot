from Src.Events.event import event
from aiogram import types
from Src.Models import User


class show_event(event):

    @staticmethod
    def activate(user: User, message: types.Message) -> str:
        print(user, message.text)
        return 'done'