from os.path import exists
from sys import platform
import sqlite3

from config.base import content_folder_name
from config.game import stats, skill
from config.database import structure, stat_structure, skill_structure


def values2sql(values: dict) -> str:
    text_sql = ", ".join(f"""{value} {'INTEGER' if values[value] == int else
                                     'TEXT' if values[value] == str else
                                     'REAL' if values[value] == float else
                                     'NUMERIC'}""" for value in values)
    return text_sql


def create_table(table_cursor: sqlite3.Cursor, table_name: str, column: dict):
    table_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({values2sql(column)})")


class Database:
    folder = f"{content_folder_name}" + "{0}{1}.db"

    skill_count = len(skill)
    stats_count = len(stats)

    def __init__(self, name_db: str):
        if platform == "win32":
            ec = "\\"
        else:
            ec = "/"

        self.name_db = self.folder.format(ec, name_db)

        if exists(self.name_db):
            self._load()
        else:
            self._create()
        self._create()

    def _load(self):
        pass

    def _create(self):
        connection = sqlite3.connect(self.name_db)
        cursor = connection.cursor()
        for table_name in structure.keys():
            create_table(cursor, table_name, structure[table_name])
        for index in range(self.skill_count):
            create_table(cursor, f"skill_{index}", skill_structure)
        for index in range(self.stats_count):
            create_table(cursor, f"stats_{index}", stat_structure)

        connection.commit()
        connection.close()

    def __str__(self):
        pass
