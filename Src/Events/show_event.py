from Src.Events.event import event
from aiogram import types
from Src.Models import User, Message
from Src.dialogue_manager import dialogue_manager


class show_event(event):
    '''
    Показательный ивент для примера.
    Выводит в консоль пользователя и сообщение.
    '''

    def activate(self, user: User, message: types.Message) -> Message:
        print(user, message.text)
        output = user.current_message
        output.text = output.text.format(event='done')

        return output