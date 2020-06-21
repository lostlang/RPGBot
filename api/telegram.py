import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import telegram_bot_kwargs
from logic.xml_work import Page

telegram_bot = Bot(**telegram_bot_kwargs)
telegram_loop = asyncio.get_event_loop()
telegram_dp = Dispatcher(telegram_bot, telegram_loop)

# Actions


@telegram_dp.message_handler(commands="start")
async def echo(message: Message):
    text = Page("ru", "start").text.text
    await message.answer(text)


@telegram_dp.message_handler()
async def echo(message: Message):
    await message.answer(message)
