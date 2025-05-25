import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

from app.handlers import rt

load_dotenv()
TOKEN = getenv("BOT_TOKEN")


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(rt)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')