from ..function.io import red
from ..function.util import get, includes

from .object import (
    ItemType, Item, Axe, Hoe, Pickaxe, Sword, Bow, Armor, TravelScroll, Pet,
)

__all__ = [
    'COLLECTION_ITEMS', 'COMPACT_ITEMS', 'OTHER_ITEMS',
    'WEAPONS', 'ARMOR_PIECES', 'TOOLS', 'TRAVEL_SCROLLS', 'PETS', 'ITEMS',
    'get_item', 'get_scroll', 'get_stack_size',
]


COLLECTION_ITEMS = [
    Item('wheat', 64, 'common'),
    Item('carrot', 64, 'common'),
    Item('potato', 64, 'common'),
    Item('pumpkin', 64, 'common'),
    Item('melon', 64, 'common'),
    Item('seeds', 64, 'common'),
    Item('mushroom', 64, 'common'),
    Item('cocoa', 64, 'common'),
    Item('cactus', 64, 'common'),
    Item('sugar_cane', 64, 'common'),
    Item('feather', 64, 'common'),
    Item('leather', 64, 'common'),
    Item('porkchop', 64, 'common'),
    Item('chicken', 64, 'common'),
    Item('mutton', 64, 'common'),
    Item('rabbit', 64, 'common'),
    Item('nether_wart', 64, 'common'),

    Item('cobblestone', 64, 'common'),
    Item('coal', 64, 'common'),
    Item('iron', 64, 'common'),
    Item('gold', 64, 'common'),
    Item('diamond', 64, 'common'),
    Item('lapis', 64, 'common'),
    Item('emerald', 64, 'common'),
    Item('redstone', 64, 'common'),
    Item('quartz', 64, 'common'),
    Item('obsidian', 64, 'common'),
    Item('glowstone', 64, 'common'),
    Item('gravel', 64, 'common'),
    Item('ice', 64, 'common'),
    Item('netherrack', 64, 'common'),
    Item('sand', 64, 'common'),
    Item('end_stone', 64, 'common'),
    Item('mithril', 64, 'common'),

    Item('rotten_flesh', 64, 'common'),
    Item('bone', 64, 'common'),
    Item('string', 64, 'common'),
    Item('spider_eye', 64, 'common'),
    Item('gunpowder', 64, 'common'),
    Item('ender_pearl', 16, 'common'),
    Item('ghast_tear', 64, 'common'),
    Item('slime_ball', 64, 'common'),
    Item('blaze_rod', 64, 'common'),
    Item('magma_cream', 64, 'common'),

    Item('oak_wood', 64, 'common'),
    Item('birch_wood', 64, 'common'),
    Item('spruce_wood', 64, 'common'),
    Item('dark_oak_wood', 64, 'common'),
    Item('acacia_wood', 64, 'common'),
    Item('jungle_wood', 64, 'common'),

    Item('fish', 64, 'common'),
    Item('salmon', 64, 'common'),
    Item('clownfish', 64, 'common'),
    Item('pufferfish', 64, 'common'),
    Item('prismarine_shard', 64, 'common'),
    Item('prismarine_crystals', 64, 'common'),
    Item('clay', 64, 'common'),
    Item('lily_pad', 64, 'common'),
    Item('ink_sack', 64, 'common'),
    Item('sponge', 64, 'common'),
]

COMPACT_ITEMS = [
    Item('hay_bale', 64, 'common'),
    Item('enchanted_bread', 64, 'common'),
    Item('golden_carrot', 64, 'common'),
    Item('glistering_melon', 64, 'common'),
    Item('mushroom_block', 64, 'common'),
    Item('wool', 64, 'common'),

    Item('enchanted_hay_bale', 64, 'uncommon'),
    Item('tightly_tied_hay_bale', 64, 'rare'),
    Item('enchanted_carrot', 64, 'uncommon'),
    Item('enchanted_golden_carrot', 64, 'uncommon'),
    Item('enchanted_potato', 64, 'uncommon'),
    Item('enchanted_baked_potato', 64, 'rare'),
    Item('enchanted_pumpkin', 64, 'uncommon'),
    Item('polished_pumpkin', 64, 'rare'),
    Item('enchanted_melon', 64, 'uncommon'),
    Item('enchanted_glistering_melon', 64, 'rare'),
    Item('enchanted_melon_block', 64, 'rare'),
    Item('enchanted_mushroom', 64, 'common'),
    Item('enchanted_mushroom_block', 64, 'common'),
    Item('enchanted_cocoa', 64, 'uncommon'),
    Item('enchanted_cookie', 64, 'rare'),
    Item('enchanted_sugar', 64, 'uncommon'),
    Item('enchanted_paper', 64, 'uncommon'),
    Item('enchanted_bookshelf', 64, 'uncommon'),
    Item('enchanted_sugar_cane', 64, 'rare'),
    Item('enchanted_feather', 64, 'uncommon'),
    Item('enchanted_beef', 64, 'uncommon'),
    Item('enchanted_leather', 64, 'uncommon'),
    Item('enchanted_pork', 64, 'uncommon'),
    Item('enchanted_grilled_pork', 64, 'rare'),
    Item('enchanted_chicken', 64, 'uncommon'),
    Item('enchanted_egg', 16, 'rare'),
    Item('enchanted_cake', 16, 'uncommon'),
    Item('super_enchanted_egg', 64, 'rare'),
    Item('enchanted_mutton', 64, 'uncommon'),
    Item('enchanted_cooked_mutton', 64, 'rare'),
    Item('enchanted_rabbit', 64, 'uncommon'),
    Item('enchanted_rabbit_foot', 64, 'uncommon'),
    Item('enchanted_rabbit_hide', 64, 'uncommon'),
    Item('enchanted_nether_wart', 64, 'uncommon'),
    Item('mutant_nether_wart', 64, 'rare'),

    Item('coal_block', 64, 'common'),
    Item('iron_block', 64, 'common'),
    Item('gold_block', 64, 'common'),
    Item('diamond_block', 64, 'common'),
    Item('lapis_block', 64, 'common'),
    Item('emerald_block', 64, 'common'),
    Item('redstone_block', 64, 'common'),
    Item('packed_ice', 64, 'common'),

    Item('enchanted_cobblestone', 64, 'uncommon'),
    Item('enchanted_coal', 64, 'uncommon'),
    Item('enchanted_iron', 64, 'uncommon'),
    Item('enchanted_gold', 64, 'uncommon'),
    Item('enchanted_diamond', 64, 'uncommon'),
    Item('enchanted_lapis', 64, 'uncommon'),
    Item('enchanted_emerald', 64, 'uncommon'),
    Item('enchanted_redstone', 64, 'uncommon'),
    Item('enchanted_quartz', 64, 'uncommon'),
    Item('enchanted_obsidian', 64, 'uncommon'),
    Item('enchanted_glowstone', 64, 'uncommon'),
    Item('enchanted_flint', 64, 'uncommon'),
    Item('enchanted_ice', 64, 'uncommon'),
    Item('enchanted_netherrack', 64, 'uncommon'),
    Item('enchanted_sand', 64, 'uncommon'),
    Item('enchanted_end_stone', 64, 'uncommon'),
    Item('enchanted_mithril', 64, 'uncommon'),

    Item('enchanted_coal_block', 64, 'rare'),
    Item('enchanted_iron_block', 64, 'rare'),
    Item('enchanted_gold_block', 64, 'rare'),
    Item('enchanted_diamond_block', 64, 'rare'),
    Item('enchanted_lapis_block', 64, 'rare'),
    Item('enchanted_emerald_block', 64, 'rare'),
    Item('enchanted_redstone_block', 64, 'rare'),
    Item('enchanted_quartz_block', 64, 'rare'),
    Item('enchanted_glowstone_block', 64, 'uncommon'),
    Item('enchanted_redstone_lamp', 64, 'rare'),
    Item('enchanted_packed_ice', 64, 'rare'),

    Item('enchanted_rotten_flesh', 64, 'uncommon'),
    Item('enchanted_bone', 64, 'uncommon'),
    Item('enchanted_string', 64, 'uncommon'),
    Item('enchanted_spider_eye', 64, 'uncommon'),
    Item('enchanted_gunpowder', 64, 'uncommon'),
    Item('enchanted_ender_pearl', 16, 'uncommon'),
    Item('enchanted_eye_of_ender', 64, 'uncommon'),
    Item('enchanted_ghast_tear', 64, 'uncommon'),
    Item('enchanted_slime_ball', 64, 'uncommon'),
    Item('enchanted_blaze_rod', 64, 'uncommon'),
    Item('enchanted_magma_cream', 64, 'uncommon'),

    Item('enchanted_oak_wood', 64, 'uncommon'),
    Item('enchanted_birch_wood', 64, 'uncommon'),
    Item('enchanted_spruce_wood', 64, 'uncommon'),
    Item('enchanted_dark_oak_wood', 64, 'uncommon'),
    Item('enchanted_acacia_wood', 64, 'uncommon'),
    Item('enchanted_jungle_wood', 64, 'uncommon'),
]

OTHER_ITEMS = [
    Item('arrow', 64, 'common'),
    Item('beef', 64, 'common'),
    Item('blaze_powder', 64, 'common'),
    Item('book', 64, 'common'),
    Item('bread', 64, 'common'),
    Item('egg', 16, 'common'),
    Item('exp_share_core', 1, 'epic'),
    Item('flint', 64, 'common'),
    Item('glowstone_block', 64, 'common'),
    Item('gold_nugget', 64, 'common'),
    Item('golden_powder', 64, 'epic'),
    Item('iron_nugget', 64, 'common'),
    Item('lapis_crystal', 1, 'rare'),
    Item('paper', 64, 'common'),
    Item('planks', 64, 'common'),
    Item('poisonous_potato', 64, 'common'),
    Item('rabbit_foot', 64, 'common'),
    Item('rabbit_hide', 64, 'common'),
    Item('stick', 64, 'common'),
    Item('sugar', 64, 'common'),
    Item('summoning_eye', 1, 'epic'),
]

WEAPONS = [
    Sword('wooden_sword', 'common', damage=20),
    Sword('golden_sword', 'common', damage=20),
    Sword('stone_sword', 'common', damage=25),
    Sword('iron_sword', 'common', damage=30),
    Sword('diamond_sword', 'uncommon', damage=35),

    Sword('undead_sword', 'common', damage=30),
    Sword('rogue_sword', 'common', damage=20),
    Sword('end_sword', 'uncommon', damage=35),
    Sword('spider_sword', 'common', damage=30),

    Sword('flaming_sword', 'uncommon', damage=50,
          strength=20),

    Sword('fancy_sword', 'common', damage=30,
          enchantments={'first_strike': 1, 'scavenger': 1,
                        'sharpness': 2, 'vampirism': 1}),
    Sword('tacticians_sword', 'rare', damage=50,
          crit_chance=20),

    Sword('raider_axe', 'rare', damage=80,
          strength=50),

    Sword('pigman_sword', 'legendary', damage=220,
          strength=100, crit_chance=5, crit_damage=30, intelligence=300),

    Sword('golem_sword', 'rare', damage=80,
          strength=125, defense=25),
    Sword('cleaver', 'uncommon', damage=40,
          strength=10),
    Sword('emerald_blade', 'epic', damage=130),
    Sword('frozen_scythe', 'rare', damage=80),
    Sword('end_stone_sword', 'epic', damage=120,
          strength=80),

    Sword('aspect_of_the_dragons', 'legendary', damage=225,
          strength=100,
          combat_skill_req=18),

    Sword('livid_dagger', 'legendary', damage=210,
          strength=60, crit_chance=100, crit_damage=50, attack_speed=50,
          dungeon_completion_req=5),

    Sword('necrons_blade', 'legendary', damage=210,
          strength=60, defense=250, intelligence=50,
          true_denfense=20, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('astraea', 'legendary', damage=210,
          strength=60, defense=250, intelligence=50,
          true_denfense=20, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('hyperion', 'legendary', damage=260,
          strength=150, intelligence=350, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('scylla', 'legendary', damage=270,
          strength=150, crit_chance=12, crit_damage=35,
          intelligence=50, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('valkyrie', 'legendary', damage=270,
          strength=145, intelligence=60, ferocity=60,
          dungeon_completion_req=7, stars=0),

    Bow('bow', 'common', damage=30),
    Bow('wither_bow', 'uncommon', damage=35),

    Bow('end_stone_bow', 'epic', damage=140,
        combat_skill_req=18),

    Bow('runaans_bow', 'legendary', damage=160,
        strength=50),
    Bow('mosquito_bow', 'legendary', damage=251,
        strength=151, crit_damage=39),
    Bow('souls_rebound', 'epic', damage=450),
]

ARMOR_PIECES = [
    Armor('leather_helmet', rarity='common', part='helmet',
          defense=5),
    Armor('leather_chestplate', rarity='common', part='chestplate',
          defense=15),
    Armor('leather_leggings', rarity='common', part='leggings',
          defense=10),
    Armor('leather_boots', rarity='common', part='boots',
          defense=5),

    Armor('golden_helmet', rarity='common', part='helmet',
          defense=10),
    Armor('golden_chestplate', rarity='common', part='chestplate',
          defense=25),
    Armor('golden_leggings', rarity='common', part='leggings',
          defense=15),
    Armor('golden_boots', rarity='common', part='boots',
          defense=5),

    Armor('chainmail_helmet', rarity='uncommon', part='helmet',
          defense=12),
    Armor('chainmail_chestplate', rarity='uncommon', part='chestplate',
          defense=30),
    Armor('chainmail_leggings', rarity='uncommon', part='leggings',
          defense=20),
    Armor('chainmail_boots', rarity='uncommon', part='boots',
          defense=7),

    Armor('iron_helmet', rarity='common', part='helmet',
          defense=10),
    Armor('iron_chestplate', rarity='common', part='chestplate',
          defense=30),
    Armor('iron_leggings', rarity='common', part='leggings',
          defense=25),
    Armor('iron_boots', rarity='common', part='boots',
          defense=10),

    Armor('diamond_helmet', rarity='uncommon', part='helmet',
          defense=15),
    Armor('diamond_chestplate', rarity='uncommon', part='chestplate',
          defense=40),
    Armor('diamond_leggings', rarity='uncommon', part='leggings',
          defense=30),
    Armor('diamond_boots', rarity='uncommon', part='boots',
          defense=15),

    Armor('farm_suit_helmet', rarity='common', part='helmet',
          defense=15),
    Armor('farm_suit_chestplate', rarity='common', part='chestplate',
          defense=40),
    Armor('farm_suit_leggings', rarity='common', part='leggings',
          defense=30),
    Armor('farm_suit_boots', rarity='common', part='boots',
          defense=15),

    Armor('farm_helmet', rarity='rare', part='helmet',
          health=20, defense=40),
    Armor('farm_chestplate', rarity='rare', part='chestplate',
          health=20, defense=75),
    Armor('farm_leggings', rarity='rare', part='leggings',
          health=20, defense=50),
    Armor('farm_boots', rarity='rare', part='boots',
          health=20, defense=35),

    Armor('pumpkin_helmet', rarity='common', part='helmet',
          health=8, defense=8),
    Armor('pumpkin_chestplate', rarity='common', part='chestplate',
          health=14, defense=14),
    Armor('pumpkin_leggings', rarity='common', part='leggings',
          health=10, defense=10),
    Armor('pumpkin_boots', rarity='common', part='boots',
          health=8, defense=8),

    Armor('farmer_boots', rarity='uncommon', part='boots',
          health=40, defense=20, speed=10),
    Armor('ranchers_boots', rarity='rare', part='boots',
          health=100, defense=70, speed=50),

    Armor('mushroom_helmet', rarity='common', part='helmet',
          health=20),
    Armor('mushroom_chestplate', rarity='common', part='chestplate',
          health=10, defense=10),
    Armor('mushroom_leggings', rarity='common', part='leggings',
          health=10, defense=5),
    Armor('mushroom_boots', rarity='common', part='boots',
          health=15),

    Armor('cactus_helmet', rarity='common', part='helmet',
          health=5, defense=10),
    Armor('cactus_chestplate', rarity='common', part='chestplate',
          health=15, defense=25),
    Armor('cactus_leggings', rarity='common', part='leggings',
          health=10, defense=20),
    Armor('cactus_boots', rarity='common', part='boots',
          health=5, defense=10),

    Armor('speedster_helmet', rarity='epic', part='helmet',
          defense=70, speed=15),
    Armor('speedster_chestplate', rarity='epic', part='chestplate',
          defense=120, speed=15),
    Armor('speedster_leggings', rarity='epic', part='leggings',
          defense=95, speed=15),
    Armor('speedster_boots', rarity='epic', part='boots',
          defense=65, speed=15),

    Armor('cow_head', rarity='common', part='helmet',
          health=15, defense=5),

    Armor('miners_outfit_helmet', rarity='uncommon', part='helmet',
          defense=15, mining_speed=25),
    Armor('miners_outfit_chestplate', rarity='uncommon', part='chestplate',
          defense=40, mining_speed=25),
    Armor('miners_outfit_leggings', rarity='uncommon', part='leggings',
          defense=30, mining_speed=25),
    Armor('miners_outfit_boots', rarity='uncommon', part='boots',
          defense=15, mining_speed=25),

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

    Armor('blaze_helmet', rarity='epic', part='helmet',
          strength=10, defense=50, speed=2),
    Armor('blaze_chestplate', rarity='epic', part='chestplate',
          strength=10, defense=150, speed=2),
    Armor('blaze_leggings', rarity='epic', part='leggings',
          strength=10, defense=110, speed=2),
    Armor('blaze_boots', rarity='epic', part='boots',
          strength=10, defense=70, speed=2),

    Armor('cheap_tuxedo_jacket', rarity='epic', part='chestplate',
          crit_damage=50, intelligence=50),
    Armor('cheap_tuxedo_pants', rarity='epic', part='leggings',
          crit_damage=25, intelligence=25),
    Armor('cheap_tuxedo_oxfords', rarity='epic', part='boots',
          crit_damage=25, intelligence=25),

    Armor('fancy_tuxedo_jacket', rarity='legendary', part='chestplate',
          crit_damage=80, intelligence=150),
    Armor('fancy_tuxedo_pants', rarity='legendary', part='leggings',
          crit_damage=35, intelligence=75),
    Armor('fancy_tuxedo_oxfords', rarity='legendary', part='boots',
          crit_damage=35, intelligence=75),

    Armor('elegant_tuxedo_jacket', rarity='legendary', part='chestplate',
          crit_damage=100, intelligence=300),
    Armor('elegant_tuxedo_pants', rarity='legendary', part='leggings',
          crit_damage=50, intelligence=100),
    Armor('elegant_tuxedo_oxfords', rarity='legendary', part='boots',
          crit_damage=50, intelligence=100, speed=10),

    Armor('lapis_helmet', rarity='uncommon', part='helmet',
          defense=25),
    Armor('lapis_chestplate', rarity='uncommon', part='chestplate',
          defense=40),
    Armor('lapis_leggings', rarity='uncommon', part='leggings',
          defense=35),
    Armor('lapis_boots', rarity='uncommon', part='boots',
          defense=20),

    Armor('miner_helmet', rarity='uncommon', part='helmet',
          defense=45),
    Armor('miner_chestplate', rarity='uncommon', part='chestplate',
          defense=95),
    Armor('miner_leggings', rarity='uncommon', part='leggings',
          defense=70),
    Armor('miner_boots', rarity='uncommon', part='boots',
          defense=45),

    Armor('ender_helmet', rarity='epic', part='helmet',
          health=20, defense=35),
    Armor('ender_chestplate', rarity='epic', part='chestplate',
          health=30, defense=60),
    Armor('ender_leggings', rarity='epic', part='leggings',
          health=25, defense=50),
    Armor('ender_boots', rarity='epic', part='boots',
          health=15, defense=25),
    Armor('obsidian_chestplate', rarity='epic', part='chestplate',
          defense=250,
          combat_skill_req=14),
]

TOOLS = [
    Axe('wooden_axe', rarity='common', tool_speed=2),
    Axe('stone_axe', rarity='common', tool_speed=4),
    Axe('golden_axe', rarity='common', tool_speed=12),
    Axe('iron_axe', rarity='common', tool_speed=6),
    Axe('diamond_axe', rarity='uncommon', tool_speed=8),

    Axe('rookie_axe', rarity='common', tool_speed=4,
        enchantments={'efficiency': 1}),
    Axe('promising_axe', rarity='uncommon', tool_speed=6),
    Axe('sweet_axe', rarity='uncommon', tool_speed=6),
    Axe('efficient_axe', rarity='uncommon', tool_speed=6),

    Hoe('wooden_hoe', rarity='common'),
    Hoe('golden_hoe', rarity='common'),
    Hoe('stone_hoe', rarity='common'),
    Hoe('iron_hoe', rarity='common'),
    Hoe('diamond_hoe', rarity='uncommon'),

    Hoe('rookie_hoe', rarity='common'),

    Pickaxe('wooden_pickaxe', rarity='common',
            breaking_power=1, mining_speed=70),
    Pickaxe('golden_pickaxe', rarity='common',
            breaking_power=1, mining_speed=250),
    Pickaxe('stone_pickaxe', rarity='common',
            breaking_power=2, mining_speed=110),
    Pickaxe('iron_pickaxe', rarity='common',
            breaking_power=3, mining_speed=160),
    Pickaxe('diamond_pickaxe', rarity='uncommon',
            breaking_power=4, mining_speed=230),

    Pickaxe('rookie_pickaxe', rarity='common',
            breaking_power=2, mining_speed=180,
            enchantments={'efficiency': 1}),
    Pickaxe('promising_pickaxe', rarity='uncommon',
            breaking_power=2, mining_speed=190),

    Pickaxe('stonk', rarity='epic',
            breaking_power=1, mining_speed=380,
            enchantments={'efficiency': 6}),
]

TRAVEL_SCROLLS = [
    TravelScroll('hub', 'hub_castle', rarity='epic'),
    TravelScroll('barn'),
    TravelScroll('desert'),
    TravelScroll('gold'),
    TravelScroll('deep'),
    TravelScroll('park'),
    TravelScroll('park', 'howl', rarity='epic'),
    TravelScroll('park', 'jungle', rarity='epic'),
    TravelScroll('spider'),
    TravelScroll('spider', 'nest', rarity='epic'),
    TravelScroll('end'),
]

PETS = [
    Pet('bee_pet', rarity='common', category='farming',
        speed=10, intelligence=50, strength=30),
    Pet('bee_pet', rarity='uncommon', category='farming',
        speed=10, intelligence=50, strength=30),
    Pet('bee_pet', rarity='rare', category='farming',
        speed=10, intelligence=50, strength=30),
    Pet('bee_pet', rarity='epic', category='farming',
        speed=10, intelligence=50, strength=30),
    Pet('bee_pet', rarity='legendary', category='farming',
        speed=10, intelligence=50, strength=30),

    Pet('hound_pet', rarity='epic', category='combat',
        strength=40, attack_speed=15, ferocity=5),
    Pet('hound_pet', rarity='legendary', category='combat',
        strength=40, attack_speed=15, ferocity=5),

    Pet('tarantula_pet', rarity='epic', category='combat',
        strength=10, crit_chance=10, crit_damage=30),
    Pet('tarantula_pet', rarity='legendary', category='combat',
        strength=10, crit_chance=10, crit_damage=30),

    Pet('enderman_pet', rarity='common', category='combat',
        crit_damage=75),
    Pet('enderman_pet', rarity='uncommon', category='combat',
        crit_damage=75),
    Pet('enderman_pet', rarity='rare', category='combat',
        crit_damage=75),
    Pet('enderman_pet', rarity='epic', category='combat',
        crit_damage=75),
    Pet('enderman_pet', rarity='legendary', category='combat',
        crit_damage=75),
    Pet('enderman_pet', rarity='mythic', category='combat',
        crit_damage=75),

    Pet('ghoul_pet', rarity='epic', category='combat',
        health=100, intelligence=70, ferocity=5),
    Pet('ghoul_pet', rarity='legendary', category='combat',
        health=100, intelligence=70, ferocity=5),
]

ITEMS = (COLLECTION_ITEMS + COMPACT_ITEMS + OTHER_ITEMS
         + WEAPONS + ARMOR_PIECES + TOOLS + TRAVEL_SCROLLS + PETS)


def get_item(name: str, **kwargs) -> ItemType:
    if not includes(ITEMS, name):
        red(f'Invalid item: {name!r}')
        exit()
    return get(ITEMS, name, **kwargs)


def get_scroll(name: str) -> TravelScroll:
    for scroll in TRAVEL_SCROLLS:
        if scroll.region is None:
            if name == scroll.island:
                return scroll
        else:
            if name == scroll.region:
                return scroll
    red(f'Invalid travel scroll: {name!r}')


def get_stack_size(name: str, /) -> int:
    return getattr(get_item(name), 'count', 1)
