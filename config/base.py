from sys import platform

telegram_bot_kwargs = {
    "token": "1147625631:AAFHWkyfED1SRiI5SFWEpT1qWGOn_fc-p0E",
    "parse_mode": "HTML"
}

content_folder_name = "content"

database_name = "rpgDB"

system_slash = "\\" if platform == "win32" else "/"
