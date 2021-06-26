from typing import Optional

from ..function.io import red
from ..function.util import get, includes

from .item import get_item, get_scroll
from .object import ItemType, Item, Mob


__all__ = ['MOBS', 'get_mob']

MOBS = [
    Mob('zombie', level=1, health=100, damage=20,
        coins=1, combat_xp=6, exp=1,
        drops=[
            (Item('rotten_flesh'), 1, 'common', 1),
            (Item('poisonous_potato'), 1, 'uncommon', 0.02),
            (Item('potato'), 1, 'rare', 0.01),
            (Item('carrot'), 1, 'rare', 0.01)]),
    Mob('skeleton', level=6, health=200, damage=47,
        coins=2, combat_xp=6, exp=4,
        drops=[
            (Item('bone'), 2, 'common', 1)]),
    Mob('wolf', level=15, health=250, damage=80,
        coins=1, combat_xp=10, exp=4,
        drops=[
            (Item('bone'), 1, 'common', 1),
            (get_item('hound_pet', rarity='epic'),
             1, 'pray_rngesus', 0.00001),
            (get_item('hound_pet', rarity='legendary'),
             1, 'pray_rngesus', 0.000003)]),
    Mob('old_wolf', level=50, health=15_000, damage=720,
        coins=40, combat_xp=40, exp=4,
        drops=[
            (Item('bone'), 1, 'common', 1),
            (get_item('hound_pet', rarity='epic'),
             1, 'pray_rngesus', 0.00001),
            (get_item('hound_pet', rarity='legendary'),
             1, 'pray_rngesus', 0.000003)]),
    Mob('crypt_ghoul', level=30, health=2_000, damage=200,
        coins=13, combat_xp=32, exp=30,
        drops=[
            (Item('rotten_flesh'), (1, 2), 'common', 1),
            (get_item('ghoul_pet', rarity='epic'),
             1, 'pray_rngesus', 0.00003),
            (get_item('ghoul_pet', rarity='legendary'),
             1, 'pray_rngesus', 0.00001)]),

    Mob('chicken', level=1, health=4, damage=0,
        coins=0, combat_xp=6, exp=2,
        drops=[
            (Item('chicken'), 1, 'common', 1),
            (Item('feather'), (1, 2), 'common', 2 / 3),
            (Item('egg'), 1, 'common', 1 / 4)]),
    Mob('cow', level=1, health=10, damage=0,
        coins=0, combat_xp=10, exp=2,
        drops=[
            (Item('beef'), (1, 3), 'common', 1),
            (Item('leather'), (1, 2), 'common', 2 / 3)]),
    Mob('mooshroom', level=1, health=10, damage=0,
        coins=0, combat_xp=0, exp=2,
        drops=[
            (Item('beef'), (1, 3), 'common', 1),
            (Item('leather'), (1, 2), 'common', 2 / 3),
            (Item('mushroom'), (1, 3), 'common', 1)]),
    Mob('pig', level=1, health=10, damage=0,
        coins=0, combat_xp=10, exp=2,
        drops=[
            (Item('porkchop'), (1, 3), 'common', 1)]),
    Mob('sheep', level=1, health=8, damage=0,
        coins=0, combat_xp=10, exp=2,
        drops=[
            (Item('mutton'), (1, 2), 'common', 1),
            (Item('wool'), 1, 'common', 1)]),
    Mob('rabbit', level=10, health=125, damage=0,
        coins=0, combat_xp=15, exp=2,
        drops=[
            (Item('rabbit'), 1, 'common', 0.6),
            (Item('rabbit_hide'), 1, 'common', 0.3),
            (Item('rabbit_foot'), 1, 'uncommon', 0.1)]),

    Mob('golden_ghoul', level=60, health=45_000, damage=500,
        coins=100, combat_xp=50, exp=30,
        drops=[
            (Item('rotten_flesh'), 2, 'common', 1),
            (Item('gold'), (1, 12), 'common', 1),
            (Item('golden_powder'), 1, 'legendary', 0.0005)]),

    Mob('sneaky_creeper', level=3, health=120, damage=80,
        coins=3, combat_xp=8, exp=3,
        drops=[
            (Item('gunpowder'), 1, 'common', 1),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('lapis_zombie', level=7, health=200, damage=50,
        coins=5, combat_xp=12, exp=10,
        drops=[
            (Item('rotten_flesh'), (1, 2), 'common', 1),
            (get_item('lapis_helmet'), 1, 'rare', 0.0025),
            (get_item('lapis_chestplate'), 1, 'rare', 0.0025),
            (get_item('lapis_leggings'), 1, 'rare', 0.0025),
            (get_item('lapis_boots'), 1, 'rare', 0.0025),
            (Item('lapis_crystal'), 1, 'rare', 0.0025),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('redstone_pigman', level=12, health=240, damage=125,
        coins=4, combat_xp=15, exp=25,
        drops=[
            (Item('gold_nugget'), 2, 'common', 1),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('small_emerald_slime', level=5, health=80, damage=70,
        coins=5, combat_xp=12, exp=20,
        drops=[
            (Item('slime_ball'), 1, 'common', 1),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('medium_emerald_slime', level=10, health=150, damage=100,
        coins=8, combat_xp=15, exp=30,
        drops=[
            (Item('slime_ball'), (1, 2), 'common', 1),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('large_emerald_slime', level=15, health=250, damage=150,
        coins=12, combat_xp=20, exp=50,
        drops=[
            (Item('slime_ball'), 2, 'common', 1),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('diamond_zombie', level=15, health=250, damage=150,
        coins=12, combat_xp=20, exp=30,
        drops=[
            (Item('rotten_flesh'), 4, 'common', 1),
            (get_item('miner_helmet'), 1, 'pray_rngesus', 0.00125),
            (get_item('miner_chestplate'), 1, 'pray_rngesus', 0.00125),
            (get_item('miner_leggings'), 1, 'pray_rngesus', 0.00125),
            (get_item('miner_boots'), 1, 'pray_rngesus', 0.00125),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('diamond_skeleton', level=15, health=250, damage=150,
        coins=12, combat_xp=20, exp=30,
        drops=[
            (Item('bone'), 4, 'common', 1),
            (get_item('miner_helmet'), 1, 'pray_rngesus', 0.00125),
            (get_item('miner_chestplate'), 1, 'pray_rngesus', 0.00125),
            (get_item('miner_leggings'), 1, 'pray_rngesus', 0.00125),
            (get_item('miner_boots'), 1, 'pray_rngesus', 0.00125),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('enchanted_diamond_zombie', level=20, health=300, damage=190,
        coins=15, combat_xp=24, exp=40,
        drops=[
            (Item('rotten_flesh'), 4, 'common', 1),
            (get_item('miner_helmet', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (get_item('miner_chestplate', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (get_item('miner_leggings', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (get_item('miner_boots', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),
    Mob('enchanted_diamond_skeleton', level=20, health=300, damage=190,
        coins=15, combat_xp=24, exp=40,
        drops=[
            (Item('bone'), 4, 'common', 1),
            (get_item('miner_helmet', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (get_item('miner_chestplate', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (get_item('miner_leggings', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (get_item('miner_boots', enchantments={'protection': 5}),
             1, 'pray_rngesus', 0.00125),
            (Item('exp_share_core'), 1, 'pray_rngesus', 0.0001)]),

    Mob('goblin', level=25, health=800, damage=300,
        coins=10, combat_xp=20, exp=50,
        drops=[
            (get_item('goblin_helmet'),
             1, 'pray_rngesus', 0.00075),
            (get_item('goblin_chestplate'),
             1, 'pray_rngesus', 0.00075),
            (get_item('goblin_leggings'),
             1, 'pray_rngesus', 0.00075),
            (get_item('goblin_boots'),
             1, 'pray_rngesus', 0.00075)]),
    Mob('ice_walker', level=45, health=8_880, damage=500,
        coins=40, combat_xp=40, exp=75,
        drops=[
            (get_item('glacite_helmet'),
             1, 'pray_rngesus', 0.0025),
            (get_item('glacite_chestplate'),
             1, 'pray_rngesus', 0.0025),
            (get_item('glacite_leggings'),
             1, 'pray_rngesus', 0.0025),
            (get_item('glacite_boots'),
             1, 'pray_rngesus', 0.0025)]),
    Mob('treasure_hoarder', level=70, health=22_000, damage=750,
        coins=50, combat_xp=70, exp=100,
        drops=[
            (Item('starfall'), (1, 2), 'common', 1),
            (Item('treasurite'), 1, 'rare', 0.005)]),
    Mob('ghost', level=100, health=1_000_000, damage=1_000,
        coins=100, combat_xp=100, exp=0,
        drops=[
            (Item('sorrow'), 1, 'rare', 0.0012),
            (Item('plasma'), 1, 'legendary', 0.001),
            (Item('bag_of_cash'), 1, 'pray_rngesus', 0.0001)]),

    Mob('pack_spirit', level=35, health=7_000, damage=450,
        coins=11, combat_xp=15, exp=10,
        drops=[
            (Item('spruce'), 1, 'uncommon', 0.15),
            (Item('dark'), 1, 'uncommon', 0.15),
            (Item('acacia'), 1, 'uncommon', 0.15),
            (get_scroll('howl'), 1, 'legendary', 0.0002),
            (get_item('hound_pet', rarity='epic'),
             1, 'pray_rngesus', 0.0002 / 3),
            (get_item('hound_pet', rarity='legendary'),
             1, 'pray_rngesus', 0.0001 / 6)]),
    Mob('soul_of_the_alpha', level=55, health=31_150, damage=1150,
        coins=50, combat_xp=50, exp=15,
        drops=[
            (Item('jungle'), 1, 'common', 1),
            (get_scroll('howl'), 1, 'legendary', 0.00035),
            (get_item('hound_pet', rarity='epic'),
             1, 'pray_rngesus', 0.0002 / 3),
            (get_item('hound_pet', rarity='legendary'),
             1, 'pray_rngesus', 0.0001 / 6)]),

    Mob('splitter_spider', level=2, health=180, damage=25,
        coins=2, combat_xp=8, exp=2,
        drops=[
            (Item('string'), (1, 2), 'common', 1),
            (Item('spider_eye'), 1, 'uncommon', 0.1)]),
    Mob('weaver_spider', level=3, health=160, damage=35,
        coins=2, combat_xp=9, exp=2,
        drops=[
            (Item('string'), 1, 'common', 1),
            (Item('spider_eye'), 1, 'uncommon', 0.1)]),
    Mob('voracious_spider', level=10, health=1_000, damage=100,
        coins=2, combat_xp=10, exp=3,
        drops=[
            (Item('string'), 1, 'common', 1),
            (Item('spider_eye'), 1, 'uncommon', 0.1)]),
    Mob('dasher_spider', level=4, health=160, damage=55,
        coins=2, combat_xp=10, exp=8,
        drops=[
            (Item('string'), 1, 'common', 1),
            (Item('spider_eye'), 1, 'common', 0.5),
            (get_scroll('nest'), 1, 'legendary', 0.0002),
            (get_item('tarantula_pet', rarity='epic'),
             1, 'pray_rngesus', 0.0001),
            (get_item('tarantula_pet', rarity='legendary'),
             1, 'pray_rngesus', 0.0001)]),
    Mob('spider_jockey', level=5, health=2530, damage=93,
        coins=7, combat_xp=14, exp=10,
        drops=[
            (Item('string'), (1, 2), 'common', 1),
            (Item('bone'), 2, 'common', 1),
            (Item('spider_eye'), 1, 'uncommon', 0.1),
            (get_item('bow'), 1, 'rare', 0.02)]),
    Mob('gravel_skeleton', level=2, health=100, damage=33,
        coins=1, combat_xp=6, exp=4,
        drops=[
            (Item('bone'), (5, 7), 'common', 1)]),
    Mob('rainy_slime', level=8, health=200, damage=100,
        coins=5, combat_xp=4, exp=5,
        drops=[
            (Item('slime_ball'), 1, 'common', 1)]),

    Mob('zombie_pigman', level=12, health=240, damage=125,
        coins=4, combat_xp=15, exp=25,
        drops=[
            (Item('gold_nugget'), 2, 'common', 1),
            (get_item('flaming_sword'), 1, 'uncommon', 0.03)]),
    Mob('mini_blaze', level=12, health=500, damage=120,
        coins=5, combat_xp=10, exp=30,
        drops=[
            (Item('blaze_rod'), 1, 'common', 1)]),
    Mob('blaze', level=15, health=600, damage=150,
        coins=10, combat_xp=10, exp=35,
        drops=[
            (Item('blaze_rod'), 2, 'common', 1),
            (get_item('blaze_hat'), 1, 'uncommon', 0.05)]),
    Mob('wither_skeleton', level=10, health=250, damage=152,
        coins=4, combat_xp=13, exp=15,
        drops=[
            (Item('bone'), 3, 'common', 1),
            (Item('coal'), 1, 'common', 0.5),
            (Item('enchanted_coal'), 1, 'rare', 0.01)]),
    Mob('small_magma_cube', level=3, health=200, damage=70,
        coins=3, combat_xp=4, exp=7,
        drops=[
            (Item('magma_cream'), 1, 'common', 1)]),
    Mob('medium_magma_cube', level=6, health=250, damage=120,
        coins=4, combat_xp=4, exp=9,
        drops=[
            (Item('magma_cream'), 1, 'common', 1)]),
    Mob('large_magma_cube', level=9, health=300, damage=150,
        coins=4, combat_xp=4, exp=20,
        drops=[
            (Item('magma_cream'), (1, 3), 'common', 1),
            (get_item('magma_cube_pet', rarity='common'),
             1, 'rare', 0.01),
            (get_item('magma_cube_pet', rarity='uncommon'),
             1, 'legendary', 0.0005),
            (get_item('magma_cube_pet', rarity='rare'),
             1, 'pray_rngesus', 0.0001)]),
    Mob('ghast', level=17, health=330, damage=150,
        coins=30, combat_xp=50, exp=32,
        drops=[
            (Item('ghast_tear'), 1, 'common', 1)]),

    Mob('enderman', level=42, health=4_500, damage=500,
        coins=10, combat_xp=40.8, exp=8,
        drops=[
            (Item('ender_pearl'), (1, 3), 'common', 1),
            (Item('enchanted_ender_pearl'), 1, 'rare', 0.01),
            (get_item('enderman_pet', rarity='common'),
             1, 'legendary', 0.0005),
            (get_item('enderman_pet', rarity='uncommon'),
             1, 'legendary', 0.0002),
            (get_item('enderman_pet', rarity='rare'),
             1, 'pray_rngesus', 0.0001),
            (get_item('ender_helmet'), 1, 'legendary', 0.00025),
            (get_item('ender_chestplate'), 1, 'legendary', 0.00025),
            (get_item('ender_leggings'), 1, 'legendary', 0.00025),
            (get_item('ender_helmet'), 1, 'legendary', 0.00025)]),
    Mob('enderman', level=45, health=6_000, damage=600,
        coins=12, combat_xp=40.8, exp=9,
        drops=[
            (Item('ender_pearl'), (1, 3), 'common', 1),
            (Item('enchanted_ender_pearl'), 1, 'rare', 0.01),
            (get_item('enderman_pet', rarity='uncommon'),
             1, 'legendary', 0.0005),
            (get_item('enderman_pet', rarity='rare'),
             1, 'legendary', 0.0002),
            (get_item('enderman_pet', rarity='epic'),
             1, 'pray_rngesus', 0.0001),
            (get_item('ender_helmet'), 1, 'legendary', 0.00025 / 3),
            (get_item('ender_chestplate'), 1, 'legendary', 0.00025 / 3),
            (get_item('ender_leggings'), 1, 'legendary', 0.00025 / 3),
            (get_item('ender_helmet'), 1, 'legendary', 0.00025 / 3)]),
    Mob('enderman', level=50, health=9_000, damage=700,
        coins=15, combat_xp=40.8, exp=10,
        drops=[
            (Item('ender_pearl'), (1, 2), 'common', 1),
            (Item('enchanted_ender_pearl'), 1, 'rare', 0.01),
            (get_item('enderman_pet', rarity='rare'),
             1, 'legendary', 0.001),
            (get_item('enderman_pet', rarity='epic'),
             1, 'pray_rngesus', 0.0001),
            (get_item('enderman_pet', rarity='legendary'),
             1, 'pray_rngesus', 0.000006),
            (get_item('ender_helmet'), 1, 'legendary', 0.00005),
            (get_item('ender_chestplate'), 1, 'legendary', 0.00005),
            (get_item('ender_leggings'), 1, 'legendary', 0.00005),
            (get_item('ender_helmet'), 1, 'legendary', 0.00005)]),
    Mob('zealot', level=55, health=13_000, damage=1250,
        coins=15, combat_xp=40, exp=10,
        drops=[
            (Item('ender_pearl'), (2, 4), 'common', 1),
            (Item('enchanted_ender_pearl'), 1, 'rare', 0.02),
            (Item('summoning_eye'), 1, 'legendary', 1 / 420)]),
    Mob('watcher', level=55, health=9_500, damage=475,
        coins=15, combat_xp=40, exp=10,
        drops=[
            (Item('arrow'), (1, 4), 'common', 1),
            (Item('ender_pearl'), (1, 2), 'common', 1),
            (Item('enchanted_bone'), 1, 'rare', 0.01),
            (get_item('end_stone_bow'), 1, 'legendary', 0.001)]),
    Mob('obsidian_defender', level=55, health=10_000, damage=200,
        coins=15, combat_xp=40, exp=10,
        drops=[
            (Item('obsidian'), (2, 3), 'common', 1),
            (Item('enchanted_obsidian'), 1, 'rare', 0.01),
            (get_item('obsidian_chestplate'), 1, 'legendary', 0.001)])]


def get_mob(name: str, **kwargs) -> Optional[ItemType]:
    if not includes(MOBS, name):
        red(f'Invalid mob: {name!r}')
        return
    return get(MOBS, name, **kwargs)
