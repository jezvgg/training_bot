from aiogram import Dispatcher, types, F, Bot
from DB.DBHelper import DBHelper
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager
from Src.Models import Message, Command
from Src.Services.telegram_service import telegram_service
from Src.settings import settings
from Src.Cron import every
from datetime import timedelta


db = DBHelper(settings.from_env())
dialogue = dialogue_manager(db.get(Message))
commands = command_manager(db.get(Command))
service = telegram_service(dialogue, commands, db)
bot = Bot(token=settings.from_env().bot_token)


@every(timedelta(days=1))
async def features_sender():
    for id, message in service.get_features().items():
        await bot.send_message(id, **service.create_answer(message))


async def command_handler(message: types.Message):
    user = service.get_user(message.from_user.id)

    print(service.get_features())
    output_message = service.handle_command(user, message)

    await message.answer(**service.create_answer(output_message)) 


async def message_handler(message: types.Message):
    user = service.get_user(message.from_user.id)

    output_message = service.handle_message(user, message)

    await message.answer(**service.create_answer(output_message))


async def callback_handler(callback: types.CallbackQuery):
    user = service.get_user(callback.from_user.id)

    output_message = service.handle_callback(user, callback)

    await callback.message.answer(**service.create_answer(output_message))


def register_handlers(dp: Dispatcher):
    dp.message.register(command_handler, F.text.startswith('/'))
    dp.message.register(message_handler, F.text)
    dp.callback_query.register(callback_handler, F.data)