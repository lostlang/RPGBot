structure = {
    "player": {"player_id": int,
               "login_player": str,
               "selected_language": str,

               "platform_id": int,
               "user_id": int},
    "player_aliases": {"main_platform_id": int,
                       "main_id": int,
                       "alias_platform_id": int,
                       "alias_id": int},
    "platform": {"platform_id": int,
                 "platform_name": str},
}

stat_structure = {
    "id_player": int,
    "is_main": bool,
    "base_value": int,
    "append_value": int,
    "buff_value": float
}

skill_structure = {
    "id_player": int,
    "level": int,
    "current_exp": int,
    "need_exp": int,
    "buff_exp": float
}
