import telegram
from aiogram import Dispatcher, Bot
import os
import asyncio

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher()

if __name__ == '__main__':
    telegram.register_handlers(dp)
    asyncio.run(dp.start_polling(bot))