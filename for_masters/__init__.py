from aiogram import Router

from for_masters.commands import router as commands_router

router = Router()

router.include_router(router=commands_router)