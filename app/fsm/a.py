from aiogram.fsm.state import StatesGroup, State


class Item(StatesGroup):
    name = State()
    day_of_subject = State()
    button = State()
