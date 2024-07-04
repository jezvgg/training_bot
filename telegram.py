from aiogram import Dispatcher, types, F, Bot
from aiogram.enums.parse_mode import ParseMode
from DB.DBHelper import DBHelper
from Src.dialogue_manager import dialogue_manager
from Src.commands_manager import command_manager
from Src.Models import Message, Command
from Src.Services.telegram_service import telegram_service
from Src.settings import settings
from Src.Cron import every
from datetime import timedelta


sets = settings.from_env()
db = DBHelper(sets)
dialogue = dialogue_manager(db.get(Message))
commands = command_manager(db.get(Command))
service = telegram_service(dialogue, commands, db)
bot = Bot(sets.bot_token)


@every(timedelta(days=1))
async def features_sender():
    '''Функция вызывается раз в день.'''
    for id, message in service.get_features().items():
        await bot.send_message(id, **service.create_answer(message), parse_mode=ParseMode.HTML)


async def command_handler(message: types.Message):
    '''Обработка команд от пользователя'''
    user = service.get_user(message.from_user.id)

    output_message = service.handle_command(user, message)

    await message.answer(**service.create_answer(output_message), parse_mode=ParseMode.HTML) 


async def message_handler(message: types.Message):
    '''Обработка всех сообщений пользователя'''
    user = service.get_user(message.from_user.id)

    output_message = service.handle_message(user, message)

    await message.answer(**service.create_answer(output_message), parse_mode=ParseMode.HTML)


async def callback_handler(callback: types.CallbackQuery):
    '''Обработка нажатия кнопок пользователя '''
    user = service.get_user(callback.from_user.id)

    output_message = service.handle_callback(user, callback)

    await callback.message.answer(**service.create_answer(output_message), parse_mode=ParseMode.HTML)


def register_handlers(dp: Dispatcher):
    '''Зарегестрировать обработчики событий'''
    dp.message.register(command_handler, F.text.startswith('/'))
    dp.message.register(message_handler, F.text)
    dp.callback_query.register(callback_handler, F.data)