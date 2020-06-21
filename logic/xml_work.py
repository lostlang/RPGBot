from os.path import exists
from sys import platform
from lxml.etree import parse, tostring, Element, SubElement, ElementTree, XMLParser

from config import xml_folder_name


class Page:
    folder = f"{xml_folder_name}" + "{0}{1}{0}{2}.xml"

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
        self.root = parse(self.name_page,
                          XMLParser(remove_blank_text=True)).getroot()
        self.text = self.root[0]
        self.keys = self.root[1]

    def _create(self):
        self.root = Element('page')
        self.text = SubElement(self.root, 'text')
        self.keys = SubElement(self.root, 'keys')

    def add_line(self):
        self.keys.append(self.line)

    def add_key(self, value, line=None):
        if line is None:
            line = -1

        if len(self.keys) == 0:
            self.add_line()

        self.keys[line].append(self.key)
        self.keys[line][-1].text = str(value)

    def save(self):
        ElementTree(self.root).write(self.name_page,
                                     encoding="utf-8")

    def __str__(self):
        return tostring(self.root, pretty_print=True).decode('utf-8')
