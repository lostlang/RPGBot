from logic.xml_work import Page
from logic.database_work import Database
from config.base import database_name, default_lang
import config.naming as naming

game_database = Database(database_name)


def return_page(lang: str, name_page: str) -> tuple:
    page = Page(lang, name_page)
    text = page.get_text()
    keys = page.get_keys()
    return text, keys


def get_player_id(platform: int, user_id: int) -> int or None:
    tables = (
        naming.player,
        naming.player_aliases,
    )
    need_column = (
        naming.player_id,
    )
    input_column = (
        naming.platform_id,
        naming.user_id
    )
    for table in tables:
        id_player = game_database.get_data(table, need_column, input_column, (platform, user_id))
        if id_player is not None:
            return id_player[0]
    else:
        return None


def get_language(player_id: int) -> str:
    lang = game_database.get_data(naming.player, (naming.player_language, ), (naming.player_id, ), (player_id, ))
    if lang is None:
        return default_lang
    else:
        return lang[0]


def start_bot(lang: str) -> tuple:
    text, keys = return_page(lang, "start")
    return text, keys


def register_player(name: str, platform: int, user_id: int):
    game_database.add_to_table(naming.player, (name, default_lang, platform, user_id))

