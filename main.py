from aiogram import Bot, Dispatcher
from asyncio import run

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from os import getenv
load_dotenv()

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

from for_users import router as user_router
from for_masters import router as master_router
from registration import router as registration_router

async def main():
    bot = Bot(token=getenv('TOKEN'), default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    dp.include_router(router=user_router)
    dp.include_router(router=master_router)
    dp.include_router(router=registration_router)

    await dp.start_polling(bot)
if __name__=="__main__":
    run(main())