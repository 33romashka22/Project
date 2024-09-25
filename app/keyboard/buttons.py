from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
week = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]


# def Week():
#     builder = InlineKeyboardBuilder()
#     for day in week:
#         builder.button(text=day, callback_data=day)
#      builder.adjust(3,2)
#      return builder.as_markup()

# def test1(days:dict):
#     builder = InlineKeyboardBuilder
#     for day in days.keys():
#         button = InlineKeyboardButton(text=day, callback_data=day)
#         builder.add(button)
#     return builder.as_markup()




def week_buttons():
    builder = InlineKeyboardBuilder()
    for day in week:
        builder.button(text=day, callback_data=day)
    builder.adjust(1)  # Відображення 1 кнопка - 1 день тижня
    return builder.as_markup()


def add_buttons():
    builder = InlineKeyboardBuilder()
    for day in week:
        builder.button(text=day, callback_data=f"day:{day}")
    builder.adjust(3,2)
    return builder.as_markup()