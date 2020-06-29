from logic.xml_work import Page
from logic.database_work import Database
from config.base import database_name, default_lang
import config.naming as naming

game_database = Database(database_name)
game_database.migrate()


def return_page(lang: str, name_page: str) -> tuple:
    page = Page(lang, name_page)
    text = page.get_text()
    keys = page.get_keys()
    return text, keys


def search_player(platform: int, user_id: int) -> int:
    need = (
        naming.player,
        (naming.player_language, )
    )
    main_table = (
        naming.platform_id,
        naming.user_id
    )
    alias_table = (
        naming.player_id,
    )

    lang = game_database.search(*need, main_table, (platform, user_id))
    if lang is None:
        lang = game_database.search(naming.player_aliases, alias_table, main_table, (platform, user_id))
    else:
        return lang[0]
    if lang is None:
        register(platform, user_id)
        return default_lang
    else:
        return game_database.search(*need, alias_table, (lang, ))


def start_bot(lang: str) -> tuple:
    text, keys = return_page(lang, "start")
    return text, keys


def register(platform: int, user_id: int):
    game_database.add_to_table(naming.player, (None, default_lang, platform, user_id))

