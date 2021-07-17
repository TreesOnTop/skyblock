from ..object import *


COMBAT_RECIPES = [
    Recipe('leather_helmet', 'combat',
           [{'name': 'leather', 'count': 5}],
           {'name': 'leather_helmet'}),
    Recipe('leather_chestplate', 'combat',
           [{'name': 'leather', 'count': 8}],
           {'name': 'leather_chestplate'}),
    Recipe('leather_leggings', 'combat',
           [{'name': 'leather', 'count': 7}],
           {'name': 'leather_leggings'}),
    Recipe('leather_boots', 'combat',
           [{'name': 'leather', 'count': 4}],
           {'name': 'leather_boots'}),

    Recipe('golden_helmet', 'combat',
           [{'name': 'gold', 'count': 5}],
           {'name': 'golden_helmet'}),
    Recipe('golden_chestplate', 'combat',
           [{'name': 'gold', 'count': 8}],
           {'name': 'golden_chestplate'}),
    Recipe('golden_leggings', 'combat',
           [{'name': 'gold', 'count': 7}],
           {'name': 'golden_leggings'}),
    Recipe('golden_boots', 'combat',
           [{'name': 'gold', 'count': 4}],
           {'name': 'golden_boots'}),

    Recipe('iron_helmet', 'combat',
           [{'name': 'iron', 'count': 5}],
           {'name': 'iron_helmet'}),
    Recipe('iron_chestplate', 'combat',
           [{'name': 'iron', 'count': 8}],
           {'name': 'iron_chestplate'}),
    Recipe('iron_leggings', 'combat',
           [{'name': 'iron', 'count': 7}],
           {'name': 'iron_leggings'}),
    Recipe('iron_boots', 'combat',
           [{'name': 'iron', 'count': 4}],
           {'name': 'iron_boots'}),

    Recipe('diamond_helmet', 'combat',
           [{'name': 'diamond', 'count': 5}],
           {'name': 'diamond_helmet'}),
    Recipe('diamond_chestplate', 'combat',
           [{'name': 'diamond', 'count': 8}],
           {'name': 'diamond_chestplate'}),
    Recipe('diamond_leggings', 'combat',
           [{'name': 'diamond', 'count': 7}],
           {'name': 'diamond_leggings'}),
    Recipe('diamond_boots', 'combat',
           [{'name': 'diamond', 'count': 4}],
           {'name': 'diamond_boots'}),

    Recipe('arrow', 'combat',
           [{'name': 'gravel'},
            {'name': 'stick'},
            {'name': 'feather'}],
           {'name': 'arrow', 'count': 4}),

    Recipe('wooden_sword', 'combat',
           [{'name': 'planks', 'count': 2},
            {'name': 'stick'}],
           {'name': 'wooden_sword'}),
    Recipe('gold_sword', 'combat',
           [{'name': 'gold', 'count': 2},
            {'name': 'stick'}],
           {'name': 'golden_sword'}),
    Recipe('stone_sword', 'combat',
           [{'name': 'cobblestone', 'count': 2},
            {'name': 'stick'}],
           {'name': 'stone_sword'}),
    Recipe('iron_sword', 'combat',
           [{'name': 'iron', 'count': 2},
            {'name': 'stick'}],
           {'name': 'iron_sword'}),
    Recipe('diamond_sword', 'combat',
           [{'name': 'diamond', 'count': 2},
            {'name': 'stick'}],
           {'name': 'diamond_sword'}),
    Recipe('bow', 'combat',
           [{'name': 'stick', 'count': 3},
            {'name': 'string', 'count': 3}],
           {'name': 'bow'}),

    Recipe('slime_ball_to_block', 'combat',
           [{'name': 'slime_ball', 'count': 9}],
           {'name': 'slime_block'}),
    Recipe('slime_block_to_ball', 'combat',
           [{'name': 'slime_block'}],
           {'name': 'slime_ball', 'count': 9}),
    Recipe('blaze_rod_to_powder', 'combat',
           [{'name': 'blaze_rod'}],
           {'name': 'blaze_powder', 'count': 2}),

    Recipe('zombie_pickaxe', 'combat',
           [{'name': 'rotten_flesh', 'count': 3},
            {'name': 'stick', 'count': 2}],
           {'name': 'zombie_pickaxe'},
           collection_req=('rotten_flesh', 2)),
    Recipe('smite_book', 'combat',
           [{'name': 'paper', 'count': 24},
            {'name': 'rotten_flesh', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'smite': 4}},
           collection_req=('rotten_flesh', 3)),
    Recipe('rotten_flesh_to_enchanted', 'combat',
           [{'name': 'rotten_flesh', 'count': 160}],
           {'name': 'enchanted_rotten_flesh'},
           collection_req=('rotten_flesh', 4)),
    Recipe('zombie_hat', 'combat',
           [{'name': 'rotten_flesh', 'count': 5}],
           {'name': 'zombie_hat'},
           collection_req=('rotten_flesh', 5)),
    Recipe('zombies_heart', 'combat',
           [{'name': 'enchanted_rotten_flesh', 'count': 256}],
           {'name': 'zombies_heart'},
           collection_req=('rotten_flesh', 6)),
    Recipe('zombie_sword', 'combat',
           [{'name': 'zombies_heart', 'count': 2},
            (Item('stick', 1))],
           {'name': 'zombie_sword'},
           collection_req=('rotten_flesh', 7)),
    Recipe('zombie_chestplate', 'combat',
           [{'name': 'zombies_heart', 'count': 4},
            {'name': 'enchanted_rotten_flesh', 'count': 4}],
           {'name': 'zombie_chestplate'},
           collection_req=('rotten_flesh', 8)),
    Recipe('zombie_leggings', 'combat',
           [{'name': 'zombies_heart', 'count': 3},
            {'name': 'enchanted_rotten_flesh', 'count': 4}],
           {'name': 'zombie_leggings'},
           collection_req=('rotten_flesh', 8)),
    Recipe('zombie_boots', 'combat',
           [{'name': 'zombies_heart', 'count': 2},
            {'name': 'enchanted_rotten_flesh', 'count': 2}],
           {'name': 'zombie_boots'},
           collection_req=('rotten_flesh', 8)),
    RecipeGroup('zombie_armor', 'combat',
                ['zombie_chestplate', 'zombie_leggings', 'zombie_boots'],
                collection_req=('rotten_flesh', 8)),
    Recipe('uncommon_zombie_pet', 'combat',
           [{'name': 'zombies_heart', 'count': 8},
            {'name': 'enchanted_egg'}],
           {'name': 'zombie_pet', 'rarity': 'uncommon'},
           collection_req=('rotten_flesh', 9)),
    Recipe('epic_zombie_pet', 'combat',
           [{'name': 'zombies_heart', 'count': 8},
            {'name': 'super_enchanted_egg'}],
           {'name': 'zombie_pet', 'rarity': 'epic'},
           collection_req=('rotten_flesh', 9)),
    RecipeGroup('zombie_pet', 'combat',
                ['uncommon_zombie_pet', 'epic_zombie_pet'],
                collection_req=('rotten_flesh', 9)),

    Recipe('power_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'bone', 'count': 40}],
           {'name': 'enchanted_book', 'enchantments': {'power': 4}},
           collection_req=('bone', 3)),
    Recipe('skeleton_hat', 'combat',
           [{'name': 'bone', 'count': 8}],
           {'name': 'skeleton_hat'},
           collection_req=('bone', 4)),
    Recipe('bone_to_enchanted', 'combat',
           [{'name': 'bone', 'count': 160}],
           {'name': 'enchanted_bone'},
           collection_req=('bone', 5)),
    Recipe('uncommon_skeleton_pet', 'combat',
           [{'name': 'enchanted_bone', 'count': 128},
            {'name': 'enchanted_egg'}],
           {'name': 'skeleton_pet', 'rarity': 'uncommon'},
           collection_req=('bone', 6)),
    Recipe('epic_skeleton_pet', 'combat',
           [{'name': 'enchanted_bone', 'count': 128},
            {'name': 'super_enchanted_egg'}],
           {'name': 'skeleton_pet', 'rarity': 'epic'},
           collection_req=('bone', 6)),
    RecipeGroup('skeleton_pet', 'combat',
                ['uncommon_skeleton_pet', 'epic_skeleton_pet'],
                collection_req=('bone', 6)),
    Recipe('hurricane_bow', 'combat',
           [{'name': 'enchanted_bone', 'count': 96},
            {'name': 'string', 'count': 96}],
           {'name': 'hurricane_bow'},
           collection_req=('bone', 7)),
    Recipe('skeletons_helmet', 'combat',
           [{'name': 'enchanted_bone', 'count': 320}],
           {'name': 'skeletons_helmet'},
           collection_req=('bone', 8)),
    Recipe('runaans_bow', 'combat',
           [{'name': 'enchanted_bone', 'count': 192},
            {'name': 'enchanted_string', 'count': 192}],
           {'name': 'runaans_bow'},
           collection_req=('bone', 9)),
    Recipe('bone_to_enchanted_block', 'combat',
           [{'name': 'enchanted_bone', 'count': 160}],
           {'name': 'enchanted_bone_block'},
           collection_req=('bone', 10)),

    Recipe('string_to_enchanted', 'combat',
           [{'name': 'string', 'count': 192}],
           {'name': 'enchanted_string'},
           collection_req=('string', 4)),
    Recipe('infinite_quiver_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'bow'}],
           {'name': 'enchanted_book', 'enchantments': {'infinite_quiver': 4}},
           collection_req=('string', 6)),
    Recipe('spiders_boots', 'combat',
           [{'name': 'enchanted_string', 'count': 256}],
           {'name': 'spiders_boots'},
           collection_req=('string', 8)),
    Recipe('uncommon_spider_pet', 'combat',
           [{'name': 'enchanted_string', 'count': 512},
            {'name': 'enchanted_egg'}],
           {'name': 'spider_pet', 'rarity': 'uncommon'},
           collection_req=('string', 9)),
    Recipe('epic_spider_pet', 'combat',
           [{'name': 'enchanted_string', 'count': 512},
            {'name': 'super_enchanted_egg'}],
           {'name': 'spider_pet', 'rarity': 'epic'},
           collection_req=('string', 9)),
    RecipeGroup('spider_pet', 'combat',
                ['uncommon_spider_pet', 'epic_spider_pet'],
                collection_req=('string', 9)),

    Recipe('spider_sword', 'combat',
           [{'name': 'spider_eye', 'count': 2},
            {'name': 'stick'}],
           {'name': 'spider_sword'},
           collection_req=('spider_eye', 2)),
    Recipe('spider_hat', 'combat',
           [{'name': 'spider_eye', 'count': 8}],
           {'name': 'spider_hat'},
           collection_req=('spider_eye', 3)),
    Recipe('spider_eye_to_enchanted', 'combat',
           [{'name': 'spider_eye', 'count': 160}],
           {'name': 'enchanted_spider_eye'},
           collection_req=('spider_eye', 4)),
    Recipe('bane_of_arthropods_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'spider_eye', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'bane_of_arthropods': 4}},
           collection_req=('spider_eye', 5)),
    Recipe('spider_eye_to_enchanted_fermented', 'combat',
           [{'name': 'enchanted_spider_eye', 'count': 64},
            {'name': 'mushroom', 'count': 64},
            {'name': 'sugar', 'count': 64}],
           {'name': 'enchanted_fermented_spider_eye'},
           collection_req=('spider_eye', 7)),
    Recipe('leaping_sword', 'combat',
           [{'name': 'enchanted_fermented_spider_eye', 'count': 24},
            {'name': 'stick'}],
           {'name': 'leaping_sword'},
           collection_req=('spider_eye', 9)),

    Recipe('creeper_hat', 'combat',
           [{'name': 'gunpowder', 'count': 8}],
           {'name': 'creeper_hat'},
           collection_req=('gunpowder', 2)),
    Recipe('blast_protection_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'gunpowder', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'blast_protection': 4}},
           collection_req=('gunpowder', 3)),
    Recipe('gunpowder_to_enchanted', 'combat',
           [{'name': 'gunpowder', 'count': 160}],
           {'name': 'enchanted_gunpowder'},
           collection_req=('gunpowder', 4)),
    Recipe('thunderlord_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'enchanted_gunpowder', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'thunderlord': 4}},
           collection_req=('gunpowder', 5)),
    Recipe('gunpowder_to_enchanted_firework', 'combat',
           [{'name': 'enchanted_gunpowder', 'count': 64},
            {'name': 'paper', 'count': 4}],
           {'name': 'enchanted_firework_rocket'},
           collection_req=('gunpowder', 6)),
    Recipe('creeper_pants', 'combat',
           [{'name': 'enchanted_gunpowder', 'count': 224}],
           {'name': 'creeper_pants'},
           collection_req=('gunpowder', 8)),
    Recipe('explosive_bow', 'combat',
           [{'name': 'enchanted_firework_rocket', 'count': 3},
            {'name': 'string', 'count': 3}],
           {'name': 'explosive_bow'},
           collection_req=('gunpowder', 9)),

    Recipe('ender_pearl_to_enchanted', 'combat',
           [{'name': 'ender_pearl', 'count': 20}],
           {'name': 'enchanted_ender_pearl'},
           collection_req=('ender_pearl', 2)),
    Recipe('ender_slayer_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'enchanted_ender_pearl', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'ender_slayer': 4}},
           collection_req=('ender_pearl', 3)),
    Recipe('ender_bow', 'combat',
           [{'name': 'enchanted_ender_pearl', 'count': 12},
            {'name': 'string', 'count': 3}],
           {'name': 'ender_bow'},
           collection_req=('ender_pearl', 5)),
    Recipe('ender_pearl_to_enchanted_eye', 'combat',
           [{'name': 'enchanted_ender_pearl', 'count': 16},
            {'name': 'blaze_powder', 'count': 64}],
           {'name': 'enchanted_eye_of_ender'},
           collection_req=('ender_pearl', 6)),
    Recipe('aspect_of_the_end', 'combat',
           [{'name': 'enchanted_eye_of_ender', 'count': 32},
            {'name': 'enchanted_diamond'}],
           {'name': 'aspect_of_the_end'},
           collection_req=('ender_pearl', 7)),
    Recipe('ender_pearl_to_absolute', 'combat',
           [{'name': 'enchanted_ender_pearl', 'count': 80}],
           {'name': 'absolute_ender_pearl'},
           collection_req=('ender_pearl', 7)),
    Recipe('ender_pearl_to_tesselated', 'combat',
           [{'name': 'absolute_ender_pearl', 'count': 80},
            {'name': 'enchanted_lapis_block', 'count': 32}],
           {'name': 'tesselated_ender_pearl'}),
    Recipe('saving_grace', 'combat',
           [{'name': 'enchanted_ender_pearl', 'count': 128},
            {'name': 'enchanted_golden_apple', 'count': 16}],
           {'name': 'saving_grace'},
           collection_req=('ender_pearl', 9)),

    Recipe('ghast_head', 'combat',
           [{'name': 'ghast_tear', 'count': 8}],
           {'name': 'ghast_head'},
           collection_req=('ghast_tear', 2)),
    Recipe('giant_killer_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'ghast_tear', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'giant_killer': 4}},
           collection_req=('ghast_tear', 3)),
    Recipe('ghast_tear_to_enchanted', 'combat',
           [{'name': 'ghast_tear', 'count': 5}],
           {'name': 'enchanted_ghast_tear'},
           collection_req=('ghast_tear', 4)),
    Recipe('vampirism_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'enchanted_ghast_tear', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'vampirism': 4}},
           collection_req=('ghast_tear', 5)),
    Recipe('silver_fang', 'combat',
           [{'name': 'enchanted_ghast_tear', 'count': 25}],
           {'name': 'silver_fang'},
           collection_req=('ghast_tear', 6)),

    Recipe('slime_hat', 'combat',
           [{'name': 'slime_ball', 'count': 8}],
           {'name': 'slime_hat'},
           collection_req=('slime_ball', 2)),
    Recipe('knockback_book', 'enchanting',
           [{'name': 'paper', 'count': 3},
            {'name': 'slime_ball', 'count': 3}],
           {'name': 'enchanted_book', 'enchantments': {'knockback': 1}},
           collection_req=('slime_ball', 3)),
    Recipe('slime_ball_to_enchanted', 'combat',
           [{'name': 'slime_ball', 'count': 160}],
           {'name': 'enchanted_slime_ball'},
           collection_req=('slime_ball', 5)),
    Recipe('punch_book', 'enchanting',
           [{'name': 'paper', 'count': 3},
            {'name': 'slime_ball'},
            {'name': 'arrow'}],
           {'name': 'enchanted_book', 'enchantments': {'punch': 1}},
           collection_req=('slime_ball', 6)),
    Recipe('slime_ball_to_enchanted_block', 'combat',
           [{'name': 'enchanted_slime_ball', 'count': 160}],
           {'name': 'enchanted_slime_block'},
           collection_req=('slime_ball', 8)),
    Recipe('slime_bow', 'combat',
           [{'name': 'enchanted_slime_block', 'count': 15},
            {'name': 'enchanted_string', 'count': 3}],
           {'name': 'slime_bow'},
           collection_req=('slime_ball', 9)),

    Recipe('blaze_hat', 'combat',
           [{'name': 'blaze_rod', 'count': 8}],
           {'name': 'blaze_hat'},
           collection_req=('blaze_rod', 2)),
    Recipe('fire_aspect_book', 'enchanting',
           [{'name': 'paper', 'count': 3},
            {'name': 'blaze_rod', 'count': 4}],
           {'name': 'enchanted_book', 'enchantments': {'fire_aspect': 1}},
           collection_req=('blaze_rod', 3)),
    Recipe('blaze_rod_to_enchanted_powder', 'combat',
           [{'name': 'blaze_rod', 'count': 160}],
           {'name': 'enchanted_blaze_powder'},
           collection_req=('blaze_rod', 4)),
    Recipe('flame_book', 'enchanting',
           [{'name': 'paper', 'count': 3},
            {'name': 'blaze_rod', 'count': 2},
            {'name': 'bow'}],
           {'name': 'enchanted_book', 'enchantments': {'flame': 1}},
           collection_req=('blaze_rod', 6)),
    Recipe('blaze_rod_to_enchanted', 'combat',
           [{'name': 'enchanted_blaze_powder', 'count': 160}],
           {'name': 'enchanted_blaze_rod'},
           collection_req=('blaze_rod', 7)),
    Recipe('blaze_helmet', 'combat',
           [{'name': 'enchanted_blaze_rod', 'count': 5}],
           {'name': 'blaze_helmet'},
           collection_req=('blaze_rod', 8)),
    Recipe('blaze_chestplate', 'combat',
           [{'name': 'enchanted_blaze_rod', 'count': 8}],
           {'name': 'blaze_chestplate'},
           collection_req=('blaze_rod', 8)),
    Recipe('blaze_leggings', 'combat',
           [{'name': 'enchanted_blaze_rod', 'count': 7}],
           {'name': 'blaze_leggings'},
           collection_req=('blaze_rod', 8)),
    Recipe('blaze_boots', 'combat',
           [{'name': 'enchanted_blaze_rod', 'count': 4}],
           {'name': 'blaze_boots'},
           collection_req=('blaze_rod', 8)),
    RecipeGroup('blaze_armor', 'combat',
                ['blaze_helmet', 'blaze_chestplate',
                 'blaze_leggings', 'blaze_boots'],
                collection_req=('blaze_rod', 8)),
    Recipe('blaze_pet', 'combat',
           [{'name': 'enchanted_blaze_rod', 'count': 64},
            {'name': 'super_enchanted_egg'}],
           {'name': 'blaze_pet', 'rarity': 'epic'},
           collection_req=('blaze_rod', 9)),

    Recipe('magma_cube_head', 'combat',
           [{'name': 'magma_cream', 'count': 8}],
           {'name': 'magma_cube_head'},
           collection_req=('magma_cream', 2)),
    Recipe('fire_protection_book', 'enchanting',
           [{'name': 'paper', 'count': 24},
            {'name': 'magma_cream', 'count': 8}],
           {'name': 'enchanted_book', 'enchantments': {'fire_protection': 4}},
           collection_req=('magma_cream', 3)),
    Recipe('magma_cream_to_enchanted', 'combat',
           [{'name': 'magma_cream', 'count': 160}],
           {'name': 'enchanted_magma_cream'},
           collection_req=('magma_cream', 5)),

    Recipe('armor_of_magma_helmet', 'combat',
           [{'name': 'enchanted_magma_cream', 'count': 60}],
           {'name': 'armor_of_magma_helmet'},
           collection_req=('magma_cream', 8)),
    Recipe('armor_of_magma_chestplate', 'combat',
           [{'name': 'enchanted_magma_cream', 'count': 96}],
           {'name': 'armor_of_magma_chestplate'},
           collection_req=('magma_cream', 8)),
    Recipe('armor_of_magma_leggings', 'combat',
           [{'name': 'enchanted_magma_cream', 'count': 84}],
           {'name': 'armor_of_magma_leggings'},
           collection_req=('magma_cream', 8)),
    Recipe('armor_of_magma_boots', 'combat',
           [{'name': 'enchanted_magma_cream', 'count': 48}],
           {'name': 'armor_of_magma_boots'},
           collection_req=('magma_cream', 8)),
    RecipeGroup('armor_of_magma', 'combat',
                ['armor_of_magma_helmet', 'armor_of_magma_chestplate',
                 'armor_of_magma_leggings', 'armor_of_magma_boots'],
                collection_req=('magma_cream', 8)),

    Recipe('magma_bow', 'combat',
           [{'name': 'enchanted_magma_cream', 'count': 96},
            {'name': 'enchanted_string', 'count': 3}],
           {'name': 'magma_bow'},
           collection_req=('magma_cream', 9)),
]
