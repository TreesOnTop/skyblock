__all__ = [
    'CUBISM_EFT',
    'BLAST_PROT_EFT', 'PROJ_PROT_EFT', 'IMPALING_EFT',
    'SEA_CREATURES',
    'ZOMBIES', 'SPIDERS', 'WOLVES', 'SKELETONS', 'DRAGONS', 'ENDERMEN', 'DRAGONS', 'END_MOBS',
    'WITHERS', 'NETHER_MOBS', 'BLAZES', 'PIGMEN', 'UNDEADS',
    'BESTIARY_ALTER',
]

CUBISM_EFT = [
    'sneaky_creeper',
    'small_emerald_slime', 'medium_emerald_slime', 'large_emerald_slime',
    'small_magma_cube', 'medium_magma_cube', 'large_magma_cube',
    'rain_slime', 'ghost',
]

BLAST_PROT_EFT = [
    'sneaky_creeper', 'large_magma_cube', 'ghast',
]

PROJ_PROT_EFT = [
    'skeleton', 'gravel_skeleton', 'watcher',
    'diamond_skeleton', 'sea_archer',
]

IMPALING_EFT = [
    'squid', 'night_squid',
    'sea_guardian', 'guardian_defender', 'sea_emperor',
]

SEA_CREATURES = [
    'squid', 'sea_walker', 'night_squid', 'sea_guardian', 'sea_witch',
    'sea_archer', 'monster_of_the_deep', 'catfish', 'sea_leech',
    'guardian_defender', 'deep_sea_protector', 'water_hydra', 'sea_emperor',
]

ZOMBIES = [
    'zombie', 'zombie_villager',
    'crypt_ghoul', 'golden_ghoul',
    'lapis_zombie', 'redstone_pigman', 'diamond_zombie',

    'revenant_horror', 'atoned_horror',
    'revenant_sycophant', 'revenant_champion', 'deformed_revenant',
    'atoned_champion', 'atoned_revenant',
]

SPIDERS = [
    'splitter_spider', 'weaver_spider', 'voracious_spider',
    'dasher_spider', 'spider_jockey',

    'tarantula_broodfather',
    'tarantula_vermin', 'tarantula_beast', 'mutant_tarantula',
]

WOLVES = [
    'wolf', 'old_wolf',
    'pack_spirit', 'howling_spirit', 'soul_of_the_alpha',

    'sven_packmaster',
    'pack_enforcer', 'sven_follower', 'sven_alpha',
]

SKELETONS = [
    'skeleton', 'diamond_skeleton',
    'gravel_skeleton', 'spider_jockey',
    'watcher', 'obsidian_defender',
    'sea_archer', 'sea_emperor',
]

ENDERMEN = [
    'enderman', 'zealot', 'voidling_fanatic', 'voidling_extremist',

    'voidgloom_seraph',
    'voidling_devotee', 'voidling_radical', 'voidcrazed_maniac',
]

DRAGONS = [
    'protector_dragon', 'old_dragon', 'wise_dragon', 'unstable_dragon',
    'young_dragon', 'strong_dragon', 'superior_dragon',
]

END_MOBS = [
    'enderman',
    'endermite',
    'zealot',
    'watcher',
    'obsidian_defender',
    'voidling_fanatic',
    'voidling_extremist',
] + DRAGONS

WITHERS = [
    'wither_skeleton',
]

NETHER_MOBS = [
    'ashfang', 'barbarian', 'barbarian_duke_x', 'bezal', 'bladesoul', 'blaze', 'dive_ghast',
    'fire_mage', 'flaming_spider', 'flare', 'ghast', 'goliath_barbarian', 'kada_knight',
    'krondor_necromancer', 'mage_outlaw', 'magma_cube_boss', 'magma_cube_rider', 'magma_cube',
    'millenia_aged_blaze', 'mushroom_bull', 'mutated_blaze', 'smoldering_blaze', 'vanquisher',
    'wither_skeleton', 'wither_spectre',
]

BLAZES = [
    'ashfang', 'bezal', 'blaze', 'flare', 'millenia_aged_blaze',
    'mutated_blaze', 'smoldering_blaze',

    'inferno_demonlord',
    'flare_demon', 'kindleheart_demon', 'burningsoul_demon',
]

PIGMEN = []

UNDEADS = ZOMBIES + SKELETONS + WITHERS

BESTIARY_ALTER = {
    'crypt_ghoul': ('crypt_ghoul', 'golden_ghoul'),
    'blaze': ('blaze', 'mini_blaze'),
    'magma_cube': ('small_magma_cube',
                   'medium_magma_cube',
                   'large_magma_cube'),
    'emerald_slime': ('small_emerald_slime',
                      'medium_emerald_slime',
                      'large_emerald_slime'),
    'miner_zombie': ('diamond_zombie',),
    'miner_skeleton': ('diamond_skeleton',),
}
