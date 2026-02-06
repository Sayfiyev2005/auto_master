from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from btns.inline_btns import markup as enter_markup

router = Router()

@router.callback_query(lambda c: c.data=="user")
async def sign_in_user(call: CallbackQuery):
    await call.answer(text="qabul qilindi")
    await call.message.delete()
    await call.message.answer(text="Shaxsiy kabinetga xush kelibsiz 😎")