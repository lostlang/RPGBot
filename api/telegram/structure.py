from aiogram.types import Message, CallbackQuery
from logic import commands
from .function import *
from .main import telegram_dp, telegram_bot

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
