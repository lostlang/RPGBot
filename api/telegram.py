import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config.base import telegram_bot_kwargs
from config.start_data_database import platforms
from logic import commands
from naming import telegram


platform_name = telegram
platform_id = platforms.index(platform_name) + 1


def keys2inline(keys):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(key, callback_data=key) for key in line]
                                                 for line in keys], resize_keyboard=True)


telegram_bot = Bot(**telegram_bot_kwargs)
telegram_loop = asyncio.get_event_loop()
telegram_dp = Dispatcher(telegram_bot, telegram_loop)


def get_id(message: Message) -> int:
    id_player = commands.get_player_id(platform_id, message.from_user.id)
    if id_player is None:
        commands.register_player(message.from_user.full_name, platform_id, message.from_user.id)
        id_player = commands.get_player_id(platform_id, message.from_user.id)
    return id_player

# Actions


@telegram_dp.message_handler(commands="start")
async def start_bot(message: Message):
    id_player = get_id(message)
    lang = commands.get_language(id_player)
    text, keys = commands.start_bot(lang)
    await message.answer(text, reply_markup=keys2inline(keys))


@telegram_dp.message_handler()
async def echo(message: Message):
    id_player = get_id(message)
    await message.answer(message)


# Callbacks


@telegram_dp.callback_query_handler()
async def echo(callback_query: CallbackQuery):
    await callback_query.answer("echo")
    await telegram_bot.send_message(chat_id=callback_query.message.chat.id,
                                    text=callback_query)
