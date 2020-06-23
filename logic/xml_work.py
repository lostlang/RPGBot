from os.path import exists
from sys import platform
from lxml.etree import parse, tostring, Element, SubElement, ElementTree, XMLParser

from config.base import content_folder_name


class Page:
    folder = f"{content_folder_name}" + "{0}{1}{0}{2}.xml"

    line = Element('line')
    key = Element('key')

    def __init__(self, lang: str, name_page: str):
        if platform == "win32":
            ec = "\\"
        else:
            ec = "/"

        self.name_page = self.folder.format(ec, lang, name_page)

        if exists(self.name_page):
            self._load()
        else:
            self._create()
            self.save()

    def _load(self):
        self._root = parse(self.name_page,
                           XMLParser(remove_blank_text=True)).getroot()
        self._text = self._root[0]
        self._keys = self._root[1]

    def _create(self):
        self._root = Element('page')
        self._text = SubElement(self._root, 'text')
        self._keys = SubElement(self._root, 'keys')

    def add_line(self):
        self._keys.append(self.line)

    def add_key(self, value, line=None):
        if line is None:
            line = -1

        if len(self._keys) == 0:
            self.add_line()

        self._keys[line].append(self.key)
        self._keys[line][-1].text = str(value)

    def get_text(self) -> str:
        text = ""
        for line in self._text.text.split('\n'):
            text = text + line.strip() + "\n"
        return text

    def get_keys(self) -> list:
        all_keys = []
        for line in self._keys:
            line_keys = []
            for key in line:
                if key.text is not None:
                    line_keys.append(key.text.strip())
            all_keys.append(line_keys)
        return all_keys

    def save(self):
        ElementTree(self._root).write(self.name_page,
                                      encoding="utf-8")

    def __str__(self):
        return tostring(self._root, pretty_print=True).decode('utf-8')
