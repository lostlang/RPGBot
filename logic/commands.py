from logic.xml_work import Page


def return_page(lang, name_page) -> tuple:
    page = Page("ru", "start")
    text = page.get_text()
    keys = page.get_keys()
    return text, keys


def start_bot():
    text, keys = return_page("ru", "start")
    return text, keys

