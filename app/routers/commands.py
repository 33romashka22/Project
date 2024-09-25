from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold
from ..data.func import open_storage, download_scedule, test_name, update_scedule, scedule

from ..data.func import f_path
from ..fsm.a import Item
from ..keyboard import *

a_router = Router()


async def answer(message: Message, text: str, keyboard, *args, **kwards):
    await message.answer(text=text, reply_markup=keyboard, **kwards)


# @a_router.message(Command("add_item"))
# async def add_item(message:Message, state:FSMContext):
#     await state.clear()
#     await state.set_state(Item.name)
#     await answer(message,"Яка назва предмету?", ReplyKeyboardRemove())
#
# @a_router.message(Item.name)
# async def item_add(message:Message, state:FSMContext):
#     await state.update_data(name=message.text)
#     open_storage(message.text, None)
#
#     await answer(message, "Повідомлення зчиталось", ReplyKeyboardRemove())
#     await state.clear()


@a_router.message(Command("add_item"))
async def item_add(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Item.name)
    await message.answer(text="Яка назва предмету?")
    current_state = await state.get_state()
    print(f"Current state: {current_state}")


@a_router.message(Item.name)
async def add_item(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Item.day_of_subject)
    open_storage(message.text, None)
    current_state = await state.get_state()
    print(f"Current state: {current_state}")


@a_router.message(Item.day_of_subject)
async def item(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Item.button)
    await answer(message, "На який день?", ReplyKeyboardRemove)


@a_router.message(Item.button)
async def add(message: Message, state: FSMContext):
    await state.clear()
    update_scedule(None, message.text, **scedule)


@a_router.message(Command("week"))
async def show_week(message: Message):
    await message.answer("Оберіть день:", reply_markup=week_buttons())


@a_router.callback_query(lambda callback: callback.data in ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"])
async def show_subjects(callback: CallbackQuery):
    day = callback.data
    scedule = download_scedule()

    subjects = scedule.get(day, ["Немає предметів на цей день"])

    subjects_text = f"Предмети на {day}: {', '.join(subjects)}"

    await callback.message.answer(subjects_text)
    await callback.answer()
