from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    name = State()
    phone_number = State()
    choose_panel = State()