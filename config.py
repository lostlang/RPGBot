
telegram_bot_kwargs = {
    "token": "1147625631:AAFHWkyfED1SRiI5SFWEpT1qWGOn_fc-p0E",
    "parse_mode": "HTML"
}

content_folder_name = "content"

database_name = "rpgDB"

structure_database = {
    "player": [{"id_player": int},
               {"platform_name": str},
               {"platform_id": int},
               {"selected_language": str},
               {"donation_rang": int}],
    "player_aliases":  [{"main_platform_name": str},
                        {"main_id": int},
                        {"alias_platform_name": str},
                        {"alias_id": int}]
}

stats_structure_database = {
    "id_player": int,
    "is_main": bool,
    "base_value": int,
    "append_value": int,
    "buff_value": float
}

skill_structure_database = {
    "id_player": int,
    "level": int,
    "current_exp": int,
    "need_exp": int,
    "buff_exp": float
}

stats = [
    "Heal point",
    "Mana point",

    "Luck",
    "Evasion",

    "Attack power",
    "Magic power",
    "Defensive power",
    "Heal power"
]

skill = [
    "Player level",

    "Luck level",
    "Evasion level",
    
    "Magic level",
    "Heal level",

    "Collecting level",
    "Crafting level",
    "Box opening level",


    "Votes level"
]
