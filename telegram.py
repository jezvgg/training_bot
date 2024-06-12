from aiogram import Dispatcher, types, F
from DB.DBHelper import DBHelper
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager
from Src.Models import Message, User, Command
from Src.event_handler import event_handler
import os


db = DBHelper(os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_HOST'],
              os.environ['DB_PORT'], os.environ['DB_NAME'])
dialogue = dialogue_manager(db.get_models(Message))
commands = command_manager(db.get_models(Command))
user: User = None


async def command_handler(message: types.Message):
    print(message.from_user.full_name)
    # Создаём нового пользователя, если его нет в БД
    if len(db.get_ones(User, message.from_user.id)) == 0:
        user_message = commands.get(message.text)
        user = User(True, False, message.from_user.full_name, user_message, False, message.from_user.id)
        db.add(user)
    else:
        user = db.get_one_model(User, message.from_user.id)
        user.current_message = commands.get(message.text)
        db.update(user)

    text = user.current_message.text

    if user.current_message.event_name:
        event = event_handler.get_event(user.current_message.event_name).activate(user, message)
        text = text.format(event=event)

    await message.answer(text)


async def message_handler(message: types.Message):
    print(message.from_user.full_name)
    # Создаём нового пользователя, если его нет в БД
    if len(db.get_ones(User, message.from_user.id)) == 0:
        user_message = dialogue.get_start()
        user = User(True, False, message.from_user.full_name, user_message, False, message.from_user.id)
        db.add(user)
    else:
        user = db.get_one_model(User, message.from_user.id)
        user.current_message = dialogue.get_next(user.current_message)
        db.update(user)

    text = user.current_message.text

    if user.current_message.event_name:
        event = event_handler.get_event(user.current_message.event_name).activate(user, message)
        text = text.format(event=event)

    await message.answer(text)


def register_handlers(dp: Dispatcher):
    dp.message.register(command_handler, F.text.startswith('/'))
    dp.message.register(message_handler, F.text)