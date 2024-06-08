from aiogram import Dispatcher, types, F
from DB.DBHelper import DBHelper
from Src.Dialogue_manager import Dialogue_manager
from Src.Models import Message, User
import os


db = DBHelper(os.environ['DB_USER'], os.environ['DB_PASSWORD'], os.environ['DB_HOST'],
              os.environ['DB_PORT'], os.environ['DB_NAME'])
manager = Dialogue_manager(db.get_models(Message))
user: User = None


async def message_handler(message: types.Message):
    print(message.from_user.full_name)
    # Создаём нового пользователя, если его нет в БД
    if len(db.get_ones(User, message.from_user.id)) == 0:
        user_message = manager.get_start()
        user = User(True, False, message.from_user.full_name, user_message, False, message.from_user.id)
        db.add(user)
    else:
        user = db.get_one_model(User, message.from_user.id)
        user.current_message = manager.get_next(user.current_message)
        db.update(user)
    print(user.current_message)

    await message.answer(user.current_message.text)


def register_handlers(dp: Dispatcher):
    dp.message.register(message_handler, F.text)