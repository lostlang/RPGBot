from os.path import exists
from re import findall
import sqlite3

from config.base import content_folder_name, system_slash
from config.game import stats, skill
from config.database_structure import structure, stat_structure, skill_structure, primary_keys, foreign_keys
from config.start_data_database import platforms


def to_column(values: dict) -> str:
    text_sql = ", ".join(f"""{value} {'INTEGER' if values[value] == int else
                                     'TEXT' if values[value] == str else
                                     'REAL' if values[value] == float else
                                     'NUMERIC'}""" for value in values)
    return text_sql


def to_primary(table_name: str) -> str:
    text_sql = ""
    if table_name in primary_keys:
        text_sql = f", PRIMARY KEY ({primary_keys[table_name]} AUTOINCREMENT)"
    return text_sql


def to_foreign(table_name: str) -> str:
    text_sql = ""
    for foreign_key in foreign_keys.keys():
        if findall(foreign_key[0], table_name):
            text_sql = text_sql + (f", FOREIGN KEY ({foreign_key[1]}) REFERENCES {foreign_keys[foreign_key][0]}"
                                   f" ({foreign_keys[foreign_key][1]})"
                                   f" ON DELETE CASCADE ON UPDATE NO ACTION")
    return text_sql


def to_search(columns: list) -> str:
    text_sql = ""
    if len(columns) > 0:
        text_sql = " WHERE " + " AND ".join([f"{name} = ?" for name in columns])
    return text_sql


def add_data(table_cursor: sqlite3.Cursor, table_name: str, column: list, text: list):
    text_sql = f"INSERT INTO {table_name} ({','.join(column)}) " \
               f"VALUES ({','.join('?' * len(text))})"
    table_cursor.execute(text_sql, text)


def search_column(table_cursor: sqlite3.Cursor, table_name: str, column_need: list, column_search: list,
                  column_value: list) -> list:
    text_sql = f"SELECT {', '.join(column_need)} FROM {table_name}" \
               f"{to_search(column_search)}"
    table_cursor.execute(text_sql, column_value)
    return table_cursor.fetchone()


def create_table(table_cursor: sqlite3.Cursor, table_name: str, column: dict):
    columns = to_column(column)
    primary_key = to_primary(table_name)
    foreign_key = to_foreign(table_name)
    text_sql = f"CREATE TABLE IF NOT EXISTS {table_name}" \
               f"({columns} {primary_key} {foreign_key})"
    table_cursor.execute(text_sql)


class Database:
    folder = f"{content_folder_name}" + "{0}{1}.db"

    skill_count = len(skill)
    stats_count = len(stats)

    def __init__(self, name_db: str):
        self.name_db = self.folder.format(system_slash, name_db)

        if not exists(self.name_db):
            self._create()

    def _open(func):
        def wrapper(*args):
            connection = sqlite3.connect(args[0].name_db)
            cursor = connection.cursor()
            out = func(*args, cursor)
            connection.commit()
            connection.close()
            return out
        return wrapper

    @_open
    def _create(self, cursor=None):
        for table_name in structure.keys():
            create_table(cursor, table_name, structure[table_name])
        for index in range(self.skill_count):
            create_table(cursor, f"skill_{index}", skill_structure)
        for index in range(self.stats_count):
            create_table(cursor, f"stat_{index}", stat_structure)
        for platform in platforms:
            add_data(cursor, "platform", ("platform_name", ), (platform, ))

    @_open
    def add_to_table(self, table_name: str, text: list, cursor=None):
        if table_name in structure.keys():
            if table_name in primary_keys.keys():
                add_data(cursor, table_name,
                         list(structure[table_name].keys())[1:],
                         text)
            else:
                add_data(cursor, table_name,
                         structure[table_name].keys(),
                         text)
        else:
            print("No")

    @_open
    def search(self, table_name: str, column_need: list, column_search: list, column_value: list, cursor=None):
        return search_column(cursor, table_name, column_need, column_search, column_value)
