from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

router = Router()

from states.state import Form
from aiogram.fsm.context import FSMContext


from btns.inline_btns import markup as enter_markup, hand_markup

@router.message(Command(commands=['start']))
async def start(msg: Message):
    await msg.answer(text=f"Botga xush kelibsiz 😊", reply_markup=hand_markup)

@router.callback_query(lambda c: c.data=="sign_in")
async def sign_in(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text="Ism, familiyangizni kiriting")
    await state.set_state(Form.name)

@router.message(Form.name)
async def get_name(msg: Message, state: FSMContext):
    name = msg.text.lower()
    if not name or name=='':
        await msg.answer(text="❌ Xatolik yuz berdi, iltimos qayta yuboring!")
        return
    await msg.answer(text=f"Telifon raqamingizni kiriting\n\n"
                          f"<i>Masalan: <u>941234567</u></i>")
    await state.set_state(Form.phone_number)

@router.message(Form.phone_number)
async def get_phone_number(msg: Message, state: FSMContext):
    phone_number = msg.text
    if not phone_number or phone_number=='' or not phone_number.isdigit() or len(phone_number)!=9:
        await msg.answer(text="❌ Xatolik yuz berdi, iltimos berilgan tartibda qayta yuboring!")
        return
    await msg.reply(text="✅ Ro'yxatdan o'tish yakunlandi")
    await state.clear()
    await msg.answer(text="Siz qaysi bo'limdasiz?", reply_markup=enter_markup)