from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Usta", callback_data="master")],
    [InlineKeyboardButton(text="Mijoz", callback_data="user")]
])

hand_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ro'yxatdan o'tish ", callback_data="sign_in")]
])