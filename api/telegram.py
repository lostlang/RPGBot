import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import telegram_bot_kwargs
from logic import commands


def keys2inline(keys):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(key, callback_data=key) for key in line]
                                                 for line in keys], resize_keyboard=True)


telegram_bot = Bot(**telegram_bot_kwargs)
telegram_loop = asyncio.get_event_loop()
telegram_dp = Dispatcher(telegram_bot, telegram_loop)

# Actions


@telegram_dp.message_handler(commands="start")
async def start_bot(message: Message):
    text, keys = commands.start_bot()
    await message.answer(text, reply_markup=keys2inline(keys))


@telegram_dp.message_handler()
async def echo(message: Message):
    await message.answer(message)


# Callbacks


@telegram_dp.callback_query_handler()
async def echo(callback_query: CallbackQuery):
    await callback_query.answer("echo")
    await telegram_bot.send_message(chat_id=callback_query.message.chat.id,
                                    text=callback_query)
