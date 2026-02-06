from aiogram import Router
from aiogram.types import CallbackQuery


router = Router()

@router.callback_query(lambda c: c.data=="master")
async def sign_in_master(call: CallbackQuery):
    await call.answer(text="qabul qilindi")
    await call.message.delete()
    await call.message.answer(text="Shaxsiy kabinetga xush kelibsiz 😎")