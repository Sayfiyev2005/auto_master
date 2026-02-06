from aiogram import Router

from for_users.commands import router as com_router

router = Router()

router.include_router(router=com_router)