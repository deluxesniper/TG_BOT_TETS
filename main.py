import asyncio
from aiogram import  Bot, Dispatcher
import logging
from handlers import router
from handlers.Config.configs import TOKEN


async def main():
    logging.basicConfig(level=logging.INFO)
    dp=Dispatcher()
    bot=Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())