from ...object import Armor


__all__ = ['MINING_ARMOR']

MINING_ARMOR = [
    Armor('miners_outfit_helmet', rarity='uncommon', part='helmet',
          defense=15,
          abilities=['miners_outfit_haste']),
    Armor('miners_outfit_chestplate', rarity='uncommon', part='chestplate',
          defense=40,
          abilities=['miners_outfit_haste']),
    Armor('miners_outfit_leggings', rarity='uncommon', part='leggings',
          defense=30,
          abilities=['miners_outfit_haste']),
    Armor('miners_outfit_boots', rarity='uncommon', part='boots',
          defense=15,
          abilities=['miners_outfit_haste']),

    Armor('golem_hat', rarity='common', part='helmet'),

    Armor('golem_armor_helmet', rarity='rare', part='helmet',
          health=45, defense=45),
    Armor('golem_armor_chestplate', rarity='rare', part='chestplate',
          health=65, defense=90),
    Armor('golem_armor_leggings', rarity='rare', part='leggings',
          health=55, defense=75),
    Armor('golem_armor_boots', rarity='rare', part='boots',
          health=40, defense=40),

    Armor('hardened_diamond_helmet', rarity='rare', part='helmet',
          defense=60),
    Armor('hardened_diamond_chestplate', rarity='rare', part='chestplate',
          defense=120),
    Armor('hardened_diamond_leggings', rarity='rare', part='leggings',
          defense=95),
    Armor('hardened_diamond_boots', rarity='rare', part='boots',
          defense=55),

    Armor('perfect_helmet', rarity='rare', part='helmet',
          defense=110),
    Armor('perfect_chestplate', rarity='rare', part='chestplate',
          defense=160),
    Armor('perfect_leggings', rarity='rare', part='leggings',
          defense=140),
    Armor('perfect_boots', rarity='rare', part='boots',
          defense=500),

    Armor('emerald_helmet', rarity='epic', part='helmet',
          defense=50),
    Armor('emerald_chestplate', rarity='epic', part='chestplate',
          defense=100),
    Armor('emerald_leggings', rarity='epic', part='leggings',
          defense=75),
    Armor('emerald_boots', rarity='epic', part='boots',
          defense=45),

    Armor('frozen_blaze_helmet', rarity='epic', part='helmet',
          strength=40, defense=110, speed=2),
    Armor('frozen_blaze_chestplate', rarity='epic', part='chestplate',
          strength=40, defense=180, speed=2),
    Armor('frozen_blaze_leggings', rarity='epic', part='leggings',
          strength=40, defense=140, speed=2),
    Armor('frozen_blaze_boots', rarity='epic', part='boots',
          strength=40, defense=100, speed=2),

    Armor('mithril_coat', rarity='epic', part='chestplate',
          defense=125, speed=15),

    Armor('lapis_helmet', rarity='uncommon', part='helmet',
          defense=25,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),
    Armor('lapis_chestplate', rarity='uncommon', part='chestplate',
          defense=40,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),
    Armor('lapis_leggings', rarity='uncommon', part='leggings',
          defense=35,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),
    Armor('lapis_boots', rarity='uncommon', part='boots',
          defense=20,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),

    Armor('miner_helmet', rarity='uncommon', part='helmet',
          defense=45),
    Armor('miner_chestplate', rarity='uncommon', part='chestplate',
          defense=95),
    Armor('miner_leggings', rarity='uncommon', part='leggings',
          defense=70),
    Armor('miner_boots', rarity='uncommon', part='boots',
          defense=45),

    Armor('goblin_helmet', rarity='rare', part='helmet',
          defense=70, intelligence=-1, mining_speed=10),
    Armor('goblin_chestplate', rarity='rare', part='chestplate',
          defense=140, intelligence=-1, mining_speed=10),
    Armor('goblin_leggings', rarity='rare', part='leggings',
          defense=125, intelligence=-1, mining_speed=10),
    Armor('goblin_boots', rarity='rare', part='boots',
          defense=60, intelligence=-1, mining_speed=10),

    Armor('glacite_helmet', rarity='rare', part='helmet',
          defense=70, speed=10, mining_speed=10, true_defense=5,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),
    Armor('glacite_chestplate', rarity='rare', part='chestplate',
          defense=150, speed=15, mining_speed=10, true_defense=20,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),
    Armor('glacite_leggings', rarity='rare', part='leggings',
          defense=125, speed=15, mining_speed=10, true_defense=20,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),
    Armor('glacite_boots', rarity='rare', part='boots',
          defense=70, speed=10, mining_speed=10, true_defense=5,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),

    Armor('sorrow_helmet', rarity='legendary', part='helmet',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=100),
    Armor('sorrow_chestplate', rarity='legendary', part='chestplate',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=200),
    Armor('sorrow_leggings', rarity='legendary', part='leggings',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=150),
    Armor('sorrow_boots', rarity='legendary', part='boots',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=75),
]
