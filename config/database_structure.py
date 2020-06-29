import config.naming as naming

structure = {
    naming.player: {naming.player_id: int,
                    naming.name: str,
                    naming.player_language: str,

                    naming.platform_id: int,
                    naming.user_id: int},
    naming.player_aliases: {naming.player_id: int,
                            naming.platform_id: int,
                            naming.user_id: int},
    naming.platform: {naming.platform_id: int,
                      naming.name: str},
    naming.stat: {naming.stat_id: int,
                  naming.name: str,
                  naming.is_primal: bool},
    naming.skill: {naming.skill_id: int,
                   naming.name: str,
                   naming.is_primal: bool}
}

stat_structure = {
    naming.player_id: int,
    naming.primal_value: int,
    naming.adaptive_value: int,
    naming.buff_value: float,
}

skill_structure = {
    naming.player_id: int,
    naming.current_level: int,
    naming.current_experience: int,
    naming.buff_value: float,
}

primary_keys = {
    naming.platform: naming.platform_id,
    naming.player: naming.player_id,
    naming.stat: naming.stat_id,
    naming.skill: naming.skill_id,
}

foreign_keys = {
    (rf"\b{naming.player}\b", naming.platform_id): (naming.platform, naming.platform_id),
    (rf"{naming.player_aliases}", naming.player_id): (naming.player, naming.player_id),
    (rf"{naming.player_aliases}", naming.platform_id): (naming.platform, naming.platform_id),
    (rf"{naming.stat}.", naming.player_id): (naming.player, naming.player_id),
    (rf"{naming.skill}.", naming.player_id): (naming.player, naming.player_id),
}


