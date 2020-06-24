structure = {
    "player": {"player_id": int,
               "login_player": str,
               "selected_language": str,

               "platform_id": int,
               "user_id": int},
    "player_aliases": {"player_id": int,
                       "platform_id": int,
                       "alias_id": int},
    "platform": {"platform_id": int,
                 "platform_name": str},
}

stat_structure = {
    "player_id": int,
    "is_main": bool,
    "base_value": int,
    "append_value": int,
    "buff_value": float,
}

skill_structure = {
    "player_id": int,
    "level": int,
    "current_exp": int,
    "need_exp": int,
    "buff_exp": float,
}

primary_keys = {
    "player": "player_id",
    "platform": "platform_id",
}

foreign_keys = {
    (r"\bplayer\b", "platform_id"): ("platform", "platform_id"),
    (r"player_aliases", "player_id"): ("player", "player_id"),
    (r"player_aliases", "platform_id"): ("platform", "platform_id"),
    (r"stat*", "player_id"): ("player", "player_id"),
    (r"skill*", "player_id"): ("player", "player_id"),
}
