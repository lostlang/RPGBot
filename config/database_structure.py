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
                   naming.is_primal: bool},
    naming.need_experience: {naming.current_level: int,
                             naming.experience: int},
    naming.bestiary: {naming.beast_id: int,
                      naming.name: str,
                      naming.min_lvl: int,
                      naming.max_lvl: int,
                      naming.base_attack: int,
                      naming.base_defense: int,
                      naming.base_evasion: int,
                      naming.stat_per_level: float},
    naming.loot: {naming.loot_id,
                  naming.name},
    naming.drop: {naming.loot_id,
                  naming.beast_id,
                  naming.current_value,
                  naming.max_value},
    naming.inventory: {naming.player_id,
                       naming.loot_id,
                       naming.current_value,
                       naming.max_value}

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
    naming.need_experience: naming.current_level,
    naming.bestiary: naming.beast_id,
    naming.loot: naming.loot_id,
}

foreign_keys = {
    (rf"\b{naming.player}\b", naming.platform_id): (naming.platform, naming.platform_id),

    (naming.player_aliases, naming.player_id): (naming.player, naming.player_id),
    (naming.player_aliases, naming.platform_id): (naming.platform, naming.platform_id),

    (rf"{naming.stat}.", naming.player_id): (naming.player, naming.player_id),
    (rf"{naming.skill}.", naming.player_id): (naming.player, naming.player_id),

    (naming.drop, naming.loot_id): (naming.loot, naming.loot_id),
    (naming.drop, naming.beast_id): (naming.bestiary, naming.beast_id),

    (naming.inventory, naming.player_id): (naming.player, naming.player_id),
    (naming.inventory, naming.loot_id): (naming.loot, naming.loot_id)
}


