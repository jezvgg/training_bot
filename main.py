import telegram
from aiogram import Dispatcher, Bot
from Src.settings import settings
import asyncio

bot = Bot(token=settings.from_env().bot_token)
dp = Dispatcher()

if __name__ == '__main__':
    telegram.register_handlers(dp)
    asyncio.run(dp.start_polling(bot))