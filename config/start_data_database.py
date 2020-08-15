import naming

platforms = (
    naming.telegram,
    naming.discord,
)

stats = (
    naming.hp,
    naming.mp,

    naming.luck,
    naming.evasion,

    naming.attack,
    naming.magic,
    naming.defense,
    naming.healing
)

skills = (
    naming.player_level,

    naming.luck_level,
    naming.evasion_level,

    naming.magic_level,
    naming.healing_level,

    naming.collecting_level,
    naming.crafting_level,
    naming.box_level,

    naming.donation_level,
    naming.vote_level
)

add_to_tables = {
    naming.platform: platforms,
    naming.stat: stats,
    naming.skill: skills
}
