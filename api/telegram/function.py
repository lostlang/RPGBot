from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from logic import commands
from config.start_data_database import platforms
from naming import telegram


def keys2inline(keys):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(key, callback_data=key) for key in line]
                                                 for line in keys], resize_keyboard=True)


def get_id(message: Message) -> int:
    platform_id = platforms.index(telegram) + 1
    id_player = commands.get_player_id(platforms.index(telegram) + 1, message.from_user.id)
    if id_player is None:
        commands.register_player(message.from_user.full_name, platform_id, message.from_user.id)
        id_player = commands.get_player_id(platform_id, message.from_user.id)
    return id_player
