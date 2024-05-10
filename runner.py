import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.parser import start_exchange_rate_scheduler
from config import TELEGRAM_BOT_TOKEN
from app.database.models import async_main
from app.handlers import router


async def main():
    start_exchange_rate_scheduler()

    await async_main()
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
