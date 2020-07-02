"""
    Storage Naming for Database.
"""

# Start structure database naming
# Table Names
player: str = "player"
platform: str = "platform"
player_aliases: str = "player_aliases"
stat: str = "stat"
skill: str = "skill"
need_experience: str = "need_experience"
bestiary: str = "bestiary"
loot: str = "loot"
drop: str = "drops"
inventory: str = "inventory"

# Column Names
# All
name: str = "name"

# Player
player_id: str = "player_id"
player_language: str = "language"
user_id: str = "user_id"

# Platform
platform_id: str = "platform_id"

# Stat & Skill
is_primal: str = "is_primal"
buff_value: str = "buff_value"

# Stat
stat_id: str = "stat_id"
primal_value: str = "primal_value"
adaptive_value: str = "adaptive_value"

# Skill
skill_id: str = "skill_id"
current_level: str = "current_level"
current_experience: str = "current_experience"

# Need experience for lvl-up
experience: str = "experience"

# Bestiary
beast_id: str = "beast_id"
min_lvl: str = "min_level"
max_lvl: str = "max_level"
base_attack: str = "base_attack"
base_defense: str = "base_defense"
base_evasion: str = "base_evasion"
stat_per_level: str = "stat"

# Loot
loot_id: str = "loot_id"

# Drop & Inventory
current_value: str = "current"
max_value: str = "max"

# End structure database naming

# Naming platforms
telegram: str = "telegram"
discord: str = "discord"

# Naming Stat
hp: str = "Heal point"
mp: str = "Mana point"
luck: str = "Luck"
evasion: str = "Evasion"
attack: str = "Attack power"
magic: str = "Magic power"
defense: str = "Defensive power"
healing: str = "Heal power"


# Naming Skill
player_level: str = "Player level"
luck_level: str = "Luck level"
evasion_level: str = "Evasion level"

magic_level: str = "Magic level"
healing_level: str = "Heal level"

collecting_level: str = "Collecting level"
crafting_level: str = "Crafting level"
box_level: str = "Box opening level"

donation_level: str = "Donation rang"
vote_level: str = "Vote level"
