import telegram
from aiogram import Dispatcher
import asyncio

dp = Dispatcher()


async def main():
    await telegram.features_sender()
    await dp.start_polling(telegram.bot)


if __name__ == '__main__':
    telegram.register_handlers(dp)
    print("Started succesfully!")
    asyncio.run(main())