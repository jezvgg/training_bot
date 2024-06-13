from aiogram import Dispatcher, types, F
from DB.DBHelper import DBHelper
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager
from Src.Models import Message, Command
from Src.Services.telegram_service import telegram_service
import os


db = DBHelper(os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_HOST'],
              os.environ['DB_PORT'], os.environ['DB_NAME'])
dialogue = dialogue_manager(db.get_models(Message))
commands = command_manager(db.get_models(Command))
service = telegram_service(dialogue, commands, db)


async def command_handler(message: types.Message):
    user = service.get_user(message.from_user.id)

    user.current_message = commands.get(message.text)
    db.update(user)

    await message.answer(**service.create_answer(user)) 


async def message_handler(message: types.Message):
    user = service.get_user(message.from_user.id)

    user.current_message = dialogue.get_next(user.current_message)
    db.update(user)

    await message.answer(**service.create_answer(user))


async def callback_handler(callback: types.CallbackQuery):
    user = service.get_user(callback.from_user.id)

    user.current_message = dialogue.get(int(callback.data))
    db.update(user)

    await callback.message.answer(**service.create_answer(user))


def register_handlers(dp: Dispatcher):
    dp.message.register(command_handler, F.text.startswith('/'))
    dp.message.register(message_handler, F.text)
    dp.callback_query.register(callback_handler, F.data)