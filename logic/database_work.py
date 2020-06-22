from os.path import exists
from sys import platform

from config import content_folder_name, structure_database


class Database:
    folder = f"{content_folder_name}" + "{0}{1}.xml"

    structure = structure_database

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
            self.save()

    def _load(self):
        pass

    def _create(self):
        pass

    def save(self):
        pass

    def __str__(self):
        pass
