from ..object import *
from ..recipe import get_recipe


FISHING_COLLECTIONS = [
    Collection(
        'fish', 'fishing',
        [
            (20, get_recipe('fish_hat')),
            (50, 5),
            (100, 10),
            (250, 25),
            (500, get_recipe('angler_armor')),
            (1_000, get_recipe('fish_to_enchanted')),
            (2_500, 250),
            (15_000, get_recipe('fish_to_enchanted_cooked')),
            (30_000, 3_000),
            (45_000, 4_500),
            (60_000, 6_000),
        ],
    ),
    Collection(
        'salmon', 'fishing',
        [
            (20, get_recipe('minnow_bait')),
            (50, 5),
            (100, get_recipe('lure_book')),
            (250, get_recipe('salmon_to_enchanted')),
            (500, get_recipe('speedster_rod')),
            (1_000, get_recipe('fish_bait')),
            (2_500, 250),
            (5_000, get_recipe('salmon_to_enchanted_cooked')),
            (10_000, get_recipe('salmon_armor')),
        ],
    ),
    Collection(
        'clownfish', 'fishing',
        [
            (10, get_recipe('clownfish_hat')),
            (25, 2.5),
            (50, get_recipe('magnet_book')),
            (100, 10),
            (200, 20),
            (400, 40),
            (800, 80),
        ],
    ),
    Collection(
        'pufferfish', 'fishing',
        [
            (20, get_recipe('pufferfish_hat')),
            (50, get_recipe('pufferfish_to_enchanted')),
            (100, get_recipe('cleave_book')),
            (150, 15),
            (400, get_recipe('spiked_bait')),
            (800, get_recipe('spiked_hook_book')),
            (2_400, 240),
            (4_800, 480),
            (9_000, 900),
        ],
    ),
    Collection(
        'prismarine_shard', 'fishing',
        [
            (10, get_recipe('impaling_book')),
            (25, get_recipe('prismarine_blade')),
            (50, get_recipe('prismarine_shard_to_enchanted')),
            (100, get_recipe('prismarine_rod')),
            (200, get_recipe('prismarine_bow')),
        ],
    ),
    Collection(
        'prismarine_crystals', 'fishing',
        [
            (10, 1),
            (25, get_recipe('light_bait')),
            (50, get_recipe('prismarine_crystals_to_enchanted')),
            (100, 10),
            (200, get_recipe('guardian_chestplate')),
            (400, get_recipe('blessed_bait')),
            (800, get_recipe('blessing_book')),
        ],
    ),
    Collection(
        'clay', 'fishing',
        [
            (50, 5),
            (100, get_recipe('clay_to_enchanted')),
            (250, 25),
            (1_000, get_recipe('frail_book')),
            (2_500, 250),
        ],
    ),
    Collection(
        'lily_pad', 'fishing',
        [
            (10, get_recipe('spooky_bait')),
            (50, get_recipe('blobfish_hat')),
            (100, get_recipe('healing_talisman')),
            (200, get_recipe('lily_pad_to_enchanted')),
            (500, get_recipe('challenging_rod')),
            (1_500, get_recipe('whale_bait')),
            (3_000, get_recipe('rod_of_champions')),
            (6_000, get_recipe('healing_ring')),
            (10_000, get_recipe('rod_of_legends')),
        ],
    ),
    Collection(
        'ink_sack', 'fishing',
        [
            (20, get_recipe('squid_hat')),
            (40, get_recipe('dark_bait')),
            (100, get_recipe('ink_sack_to_enchanted')),
            (200, 20),
            (400, get_recipe('caster_book')),
            (800, 80),
            (1_500, get_recipe('angler_book')),
            (2_500, 250),
            (4_000, get_recipe('ink_wand')),
        ],
    ),
    Collection(
        'sponge', 'fishing',
        [
            (20, get_recipe('sponge_rod')),
            (40, 4),
            (100, get_recipe('sponge_to_enchanted')),
            (200, get_recipe('sea_creature_talisman')),
            (400, get_recipe('stereo_pants')),
            (800, get_recipe('sea_creature_ring')),
            (1_500, get_recipe('sponge_to_enchanted_wet')),
            (2_500, get_recipe('sea_creature_artifact')),
            (4_000, get_recipe('sponge_armor')),
        ],
    ),
]
