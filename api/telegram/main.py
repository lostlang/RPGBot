import asyncio
from aiogram import Bot, Dispatcher
from config.base import telegram_bot_kwargs


telegram_bot = Bot(**telegram_bot_kwargs)
telegram_loop = asyncio.get_event_loop()
telegram_dp = Dispatcher(telegram_bot, telegram_loop)

