from os import getenv

from dotenv import load_dotenv

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.types import Message, BotCommand
from aiogram.utils.markdown import *
from aiogram.client.bot import *
from .routers import *
from .routers.commands import a_router
b_router = Router()
b_router.include_router(a_router)
load_dotenv()

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start Bot"),
        BotCommand(command="/help", description="Виводить список усіх комманд і що вони роблять"),
        BotCommand(command="/add_item", description="Додати предмет")
    ]

    await bot.set_my_commands(commands)


@b_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await set_commands((message.bot))
    await message.answer(f"Вітаю у нашому боті: {hbold(message.from_user.full_name)}!")

@b_router.message(lambda message: message.text == '/help')
async def command_help_handler(message: Message) -> None:
    help_text = (
        "All commands:\n"
        "/start - Start Bot\n"     
        ""
    )

    await message.answer(help_text)


async def main() -> None:
    TOKEN = getenv("BOT_TOKEN")


    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(b_router)

    await dp.start_polling(bot)
