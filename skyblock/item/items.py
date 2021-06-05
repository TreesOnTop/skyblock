from typing import Any

from ..function.util import get

from .object import ItemType, Item, Pickaxe, Axe, Sword, Armor, Pet

__all__ = [
    'COLLECTIONS', 'WEAPONS', 'TOOLS', 'ALL_ITEM', 'get_item',
]


COLLECTIONS = [
    Item('wheat', 64, 'common'),
    Item('carrot', 64, 'common'),
    Item('potato', 64, 'common'),
    Item('pumpkin', 64, 'common'),
    Item('melon', 64, 'common'),
    Item('seeds', 64, 'common'),
    Item('red_mushroom', 64, 'common'),
    Item('brown_mushroom', 64, 'common'),
    Item('cocoa_beans', 64, 'common'),
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
    Item('iron_ingot', 64, 'common'),
    Item('gold_ingot', 64, 'common'),
    Item('diamond', 64, 'common'),
    Item('lapis_lazuli', 64, 'common'),
    Item('emerald', 64, 'common'),
    Item('redstone', 64, 'common'),
    Item('quartz', 64, 'common'),
    Item('obsidian', 64, 'common'),
    Item('glowstone_dust', 64, 'common'),
    Item('gravel', 64, 'common'),
    Item('ice', 64, 'common'),
    Item('netherrack', 64, 'common'),
    Item('sand', 64, 'common'),
    Item('endstone', 64, 'common'),
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
]

COMPACT = [
    Item('enchanted_ender_pearl', 16, 'uncommon'),
    Item('enchanted_eye_of_ender', 64, 'uncommon'),
]

WEAPONS = [
    Sword('raider_axe', 'rare',
          damage=80, strength=50),

    Sword('aspect_of_the_dragons', 'legendary',
          damage=225, strength=100,
          combat_skill_req=18),

    Sword('livid_dagger', 'legendary',
          damage=210, strength=60, crit_chance=100, crit_damage=50,
          attack_speed=50,
          dungeon_completion_req=5),

    Sword('necrons_blade', 'legendary',
          damage=210, strength=60,
          defense=250, intelligence=50, true_denfense=20, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('astraea', 'legendary',
          damage=210, strength=60,
          defense=250, intelligence=50, true_denfense=20, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('hyperion', 'legendary',
          damage=260, strength=150,
          intelligence=350, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('scylla', 'legendary',
          damage=270, strength=150, crit_chance=12, crit_damage=35,
          intelligence=50, ferocity=30,
          dungeon_completion_req=7, stars=0),
    Sword('valkyrie', 'legendary',
          damage=270, strength=145,
          intelligence=60, ferocity=60,
          dungeon_completion_req=7, stars=0),

    Sword('runaans_bow', 'legendary',
          damage=160, strength=50),
    Sword('mosquito_bow', 'legendary',
          damage=251, strength=151, crit_damage=39),
    Sword('souls_rebound', 'epic',
          damage=450),
]

ARMOR_PIECES = [
    Armor('ender_helmet', rarity='epic', part='helmet',
          health=20, defense=35),
    Armor('ender_chestplate', rarity='epic', part='chestplate',
          health=30, defense=60),
    Armor('ender_leggings', rarity='epic', part='leggings',
          health=25, defense=50),
    Armor('ender_boots', rarity='epic', part='boots',
          health=15, defense=25),
]

TOOLS = [
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

    Axe('wooden_axe', rarity='common', tool_speed=2),
    Axe('stone_axe', rarity='common', tool_speed=4),
    Axe('golden_axe', rarity='common', tool_speed=12),
    Axe('iron_axe', rarity='common', tool_speed=6),
    Axe('wooden_axe', rarity='uncommon', tool_speed=8),
]

PETS = [
    Pet('enderman_pet', rarity='common',
        crit_damage=75),
    Pet('enderman_pet', rarity='uncommon',
        crit_damage=75),
    Pet('enderman_pet', rarity='rare',
        crit_damage=75),
    Pet('enderman_pet', rarity='epic',
        crit_damage=75),
    Pet('enderman_pet', rarity='legendary',
        crit_damage=75),
    Pet('enderman_pet', rarity='mythic',
        crit_damage=75),
]

ALL_ITEM = COLLECTIONS + WEAPONS + ARMOR_PIECES + TOOLS + PETS


def get_item(name: str, default: Any = None, **kwargs) -> ItemType:
    for item in ALL_ITEM:
        if item.name == name:
            for kwarg in kwargs:
                if getattr(item, kwarg, None) != kwargs[kwarg]:
                    break
            else:
                return item.copy()
    return default.copy() if hasattr(default, 'copy') else default
