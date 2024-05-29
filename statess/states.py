from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    language = State()
    phone = State()
