# coding=utf-8
"""Module holding all currently useable Materials as well utilities for them """
from enum import Enum

from classes.datafile.Parser import Parser


@Parser.Parser(
    file='blocks.json',
    directory='data/minecraft/{version}/reports/',
    struct={
        'properties': {
            '_action': {
                'type': 'call_method',
                'method': 'action_properties',
            },
        },
        'states': {
            '_action': {
                'type': 'call_method',
                'method': 'action_states',
            },
        },
    },
    key_pattern='minecraft:{key}'
)
class Material(Enum):
    """ Represents a Material -
    Materials should be compared by entity, not by value"""

    def __init__(self, namespace_id):
        self.namespace_id = namespace_id

    def action_properties(self, save_struct, properties):
        # Save a flat version of properties
        flat_properties = Material._elem_flat(properties)
        save_struct['flat_properties'] = flat_properties

        # Save datas
        save_struct['properties'] = properties

    @staticmethod
    def _elem_flat(elem):
        return [e for e in elem]

    def action_states(self, save_struct, elem):
        if 'ids' not in save_struct:
            save_struct['ids'] = {}
            save_struct['states'] = {}
        for state in elem:
            state_properties = state['properties'] if 'properties' in state else None
            id = state['id']
            if 'default' in state and state['default']:
                save_struct['default'] = id
            flat_state = Material._flat_properties_state(save_struct['properties'], state_properties) if state_properties is not None else []
            save_struct['ids'][id] = flat_state
            save_struct['states'] = Material._save_flat_state(flat_state, id, save_struct['states'])

    @staticmethod
    def _flat_properties_state(properties, states, default=None):
        return [states[prop] if prop in states else default for prop in properties]

    @staticmethod
    def _save_flat_state(flat_state, id, save_struct):
        save_struct = save_struct if save_struct is not None else {}
        if len(flat_state) == 0:
            return id
        else:
            if flat_state[0] not in save_struct:
                save_struct[flat_state[0]] = {}
            save_struct[flat_state[0]] = Material._save_flat_state(flat_state[1:], id, save_struct[flat_state[0]])
        return save_struct

    ACACIA_BUTTON = ('acacia_button')
    ACACIA_DOOR = ('acacia_door')
    ACACIA_FENCE = ('acacia_fence')
    ACACIA_FENCE_GATE = ('acacia_fence_gate')
    ACACIA_LEAVES = ('acacia_leaves')
    ACACIA_LOG = ('acacia_log')
    ACACIA_PLANKS = ('acacia_planks')
    ACACIA_PRESSURE_PLATE = ('acacia_pressure_plate')
    ACACIA_SAPLING = ('acacia_sapling')
    ACACIA_SIGN = ('acacia_sign')
    ACACIA_SLAB = ('acacia_slab')
    ACACIA_STAIRS = ('acacia_stairs')
    ACACIA_TRAPDOOR = ('acacia_trapdoor')
    ACACIA_WALL_SIGN = ('acacia_wall_sign')
    ACACIA_WOOD = ('acacia_wood')
    ACTIVATOR_RAIL = ('activator_rail')
    AIR = ('air')
    ALLIUM = ('allium')
    ANDESITE = ('andesite')
    ANDESITE_SLAB = ('andesite_slab')
    ANDESITE_STAIRS = ('andesite_stairs')
    ANDESITE_WALL = ('andesite_wall')
    ANVIL = ('anvil')
    ATTACHED_MELON_STEM = ('attached_melon_stem')
    ATTACHED_PUMPKIN_STEM = ('attached_pumpkin_stem')
    AZURE_BLUET = ('azure_bluet')
    BAMBOO = ('bamboo')
    BAMBOO_SAPLING = ('bamboo_sapling')
    BARREL = ('barrel')
    BARRIER = ('barrier')
    BEACON = ('beacon')
    BEDROCK = ('bedrock')
    BEEHIVE = ('beehive')
    BEETROOTS = ('beetroots')
    BEE_NEST = ('bee_nest')
    BELL = ('bell')
    BIRCH_BUTTON = ('birch_button')
    BIRCH_DOOR = ('birch_door')
    BIRCH_FENCE = ('birch_fence')
    BIRCH_FENCE_GATE = ('birch_fence_gate')
    BIRCH_LEAVES = ('birch_leaves')
    BIRCH_LOG = ('birch_log')
    BIRCH_PLANKS = ('birch_planks')
    BIRCH_PRESSURE_PLATE = ('birch_pressure_plate')
    BIRCH_SAPLING = ('birch_sapling')
    BIRCH_SIGN = ('birch_sign')
    BIRCH_SLAB = ('birch_slab')
    BIRCH_STAIRS = ('birch_stairs')
    BIRCH_TRAPDOOR = ('birch_trapdoor')
    BIRCH_WALL_SIGN = ('birch_wall_sign')
    BIRCH_WOOD = ('birch_wood')
    BLACK_BANNER = ('black_banner')
    BLACK_BED = ('black_bed')
    BLACK_CARPET = ('black_carpet')
    BLACK_CONCRETE = ('black_concrete')
    BLACK_CONCRETE_POWDER = ('black_concrete_powder')
    BLACK_GLAZED_TERRACOTTA = ('black_glazed_terracotta')
    BLACK_SHULKER_BOX = ('black_shulker_box')
    BLACK_STAINED_GLASS = ('black_stained_glass')
    BLACK_STAINED_GLASS_PANE = ('black_stained_glass_pane')
    BLACK_TERRACOTTA = ('black_terracotta')
    BLACK_WALL_BANNER = ('black_wall_banner')
    BLACK_WOOL = ('black_wool')
    BLAST_FURNACE = ('blast_furnace')
    BLUE_BANNER = ('blue_banner')
    BLUE_BED = ('blue_bed')
    BLUE_CARPET = ('blue_carpet')
    BLUE_CONCRETE = ('blue_concrete')
    BLUE_CONCRETE_POWDER = ('blue_concrete_powder')
    BLUE_GLAZED_TERRACOTTA = ('blue_glazed_terracotta')
    BLUE_ICE = ('blue_ice')
    BLUE_ORCHID = ('blue_orchid')
    BLUE_SHULKER_BOX = ('blue_shulker_box')
    BLUE_STAINED_GLASS = ('blue_stained_glass')
    BLUE_STAINED_GLASS_PANE = ('blue_stained_glass_pane')
    BLUE_TERRACOTTA = ('blue_terracotta')
    BLUE_WALL_BANNER = ('blue_wall_banner')
    BLUE_WOOL = ('blue_wool')
    BONE_BLOCK = ('bone_block')
    BOOKSHELF = ('bookshelf')
    BRAIN_CORAL = ('brain_coral')
    BRAIN_CORAL_BLOCK = ('brain_coral_block')
    BRAIN_CORAL_FAN = ('brain_coral_fan')
    BRAIN_CORAL_WALL_FAN = ('brain_coral_wall_fan')
    BREWING_STAND = ('brewing_stand')
    BRICKS = ('bricks')
    BRICK_SLAB = ('brick_slab')
    BRICK_STAIRS = ('brick_stairs')
    BRICK_WALL = ('brick_wall')
    BROWN_BANNER = ('brown_banner')
    BROWN_BED = ('brown_bed')
    BROWN_CARPET = ('brown_carpet')
    BROWN_CONCRETE = ('brown_concrete')
    BROWN_CONCRETE_POWDER = ('brown_concrete_powder')
    BROWN_GLAZED_TERRACOTTA = ('brown_glazed_terracotta')
    BROWN_MUSHROOM = ('brown_mushroom')
    BROWN_MUSHROOM_BLOCK = ('brown_mushroom_block')
    BROWN_SHULKER_BOX = ('brown_shulker_box')
    BROWN_STAINED_GLASS = ('brown_stained_glass')
    BROWN_STAINED_GLASS_PANE = ('brown_stained_glass_pane')
    BROWN_TERRACOTTA = ('brown_terracotta')
    BROWN_WALL_BANNER = ('brown_wall_banner')
    BROWN_WOOL = ('brown_wool')
    BUBBLE_COLUMN = ('bubble_column')
    BUBBLE_CORAL = ('bubble_coral')
    BUBBLE_CORAL_BLOCK = ('bubble_coral_block')
    BUBBLE_CORAL_FAN = ('bubble_coral_fan')
    BUBBLE_CORAL_WALL_FAN = ('bubble_coral_wall_fan')
    CACTUS = ('cactus')
    CAKE = ('cake')
    CAMPFIRE = ('campfire')
    CARROTS = ('carrots')
    CARTOGRAPHY_TABLE = ('cartography_table')
    CARVED_PUMPKIN = ('carved_pumpkin')
    CAULDRON = ('cauldron')
    CAVE_AIR = ('cave_air')
    CHAIN_COMMAND_BLOCK = ('chain_command_block')
    CHEST = ('chest')
    CHIPPED_ANVIL = ('chipped_anvil')
    CHISELED_QUARTZ_BLOCK = ('chiseled_quartz_block')
    CHISELED_RED_SANDSTONE = ('chiseled_red_sandstone')
    CHISELED_SANDSTONE = ('chiseled_sandstone')
    CHISELED_STONE_BRICKS = ('chiseled_stone_bricks')
    CHORUS_FLOWER = ('chorus_flower')
    CHORUS_PLANT = ('chorus_plant')
    CLAY = ('clay')
    COAL_BLOCK = ('coal_block')
    COAL_ORE = ('coal_ore')
    COARSE_DIRT = ('coarse_dirt')
    COBBLESTONE = ('cobblestone')
    COBBLESTONE_SLAB = ('cobblestone_slab')
    COBBLESTONE_STAIRS = ('cobblestone_stairs')
    COBBLESTONE_WALL = ('cobblestone_wall')
    COBWEB = ('cobweb')
    COCOA = ('cocoa')
    COMMAND_BLOCK = ('command_block')
    COMPARATOR = ('comparator')
    COMPOSTER = ('composter')
    CONDUIT = ('conduit')
    CORNFLOWER = ('cornflower')
    CRACKED_STONE_BRICKS = ('cracked_stone_bricks')
    CRAFTING_TABLE = ('crafting_table')
    CREEPER_HEAD = ('creeper_head')
    CREEPER_WALL_HEAD = ('creeper_wall_head')
    CUT_RED_SANDSTONE = ('cut_red_sandstone')
    CUT_RED_SANDSTONE_SLAB = ('cut_red_sandstone_slab')
    CUT_SANDSTONE = ('cut_sandstone')
    CUT_SANDSTONE_SLAB = ('cut_sandstone_slab')
    CYAN_BANNER = ('cyan_banner')
    CYAN_BED = ('cyan_bed')
    CYAN_CARPET = ('cyan_carpet')
    CYAN_CONCRETE = ('cyan_concrete')
    CYAN_CONCRETE_POWDER = ('cyan_concrete_powder')
    CYAN_GLAZED_TERRACOTTA = ('cyan_glazed_terracotta')
    CYAN_SHULKER_BOX = ('cyan_shulker_box')
    CYAN_STAINED_GLASS = ('cyan_stained_glass')
    CYAN_STAINED_GLASS_PANE = ('cyan_stained_glass_pane')
    CYAN_TERRACOTTA = ('cyan_terracotta')
    CYAN_WALL_BANNER = ('cyan_wall_banner')
    CYAN_WOOL = ('cyan_wool')
    DAMAGED_ANVIL = ('damaged_anvil')
    DANDELION = ('dandelion')
    DARK_OAK_BUTTON = ('dark_oak_button')
    DARK_OAK_DOOR = ('dark_oak_door')
    DARK_OAK_FENCE = ('dark_oak_fence')
    DARK_OAK_FENCE_GATE = ('dark_oak_fence_gate')
    DARK_OAK_LEAVES = ('dark_oak_leaves')
    DARK_OAK_LOG = ('dark_oak_log')
    DARK_OAK_PLANKS = ('dark_oak_planks')
    DARK_OAK_PRESSURE_PLATE = ('dark_oak_pressure_plate')
    DARK_OAK_SAPLING = ('dark_oak_sapling')
    DARK_OAK_SIGN = ('dark_oak_sign')
    DARK_OAK_SLAB = ('dark_oak_slab')
    DARK_OAK_STAIRS = ('dark_oak_stairs')
    DARK_OAK_TRAPDOOR = ('dark_oak_trapdoor')
    DARK_OAK_WALL_SIGN = ('dark_oak_wall_sign')
    DARK_OAK_WOOD = ('dark_oak_wood')
    DARK_PRISMARINE = ('dark_prismarine')
    DARK_PRISMARINE_SLAB = ('dark_prismarine_slab')
    DARK_PRISMARINE_STAIRS = ('dark_prismarine_stairs')
    DAYLIGHT_DETECTOR = ('daylight_detector')
    DEAD_BRAIN_CORAL = ('dead_brain_coral')
    DEAD_BRAIN_CORAL_BLOCK = ('dead_brain_coral_block')
    DEAD_BRAIN_CORAL_FAN = ('dead_brain_coral_fan')
    DEAD_BRAIN_CORAL_WALL_FAN = ('dead_brain_coral_wall_fan')
    DEAD_BUBBLE_CORAL = ('dead_bubble_coral')
    DEAD_BUBBLE_CORAL_BLOCK = ('dead_bubble_coral_block')
    DEAD_BUBBLE_CORAL_FAN = ('dead_bubble_coral_fan')
    DEAD_BUBBLE_CORAL_WALL_FAN = ('dead_bubble_coral_wall_fan')
    DEAD_BUSH = ('dead_bush')
    DEAD_FIRE_CORAL = ('dead_fire_coral')
    DEAD_FIRE_CORAL_BLOCK = ('dead_fire_coral_block')
    DEAD_FIRE_CORAL_FAN = ('dead_fire_coral_fan')
    DEAD_FIRE_CORAL_WALL_FAN = ('dead_fire_coral_wall_fan')
    DEAD_HORN_CORAL = ('dead_horn_coral')
    DEAD_HORN_CORAL_BLOCK = ('dead_horn_coral_block')
    DEAD_HORN_CORAL_FAN = ('dead_horn_coral_fan')
    DEAD_HORN_CORAL_WALL_FAN = ('dead_horn_coral_wall_fan')
    DEAD_TUBE_CORAL = ('dead_tube_coral')
    DEAD_TUBE_CORAL_BLOCK = ('dead_tube_coral_block')
    DEAD_TUBE_CORAL_FAN = ('dead_tube_coral_fan')
    DEAD_TUBE_CORAL_WALL_FAN = ('dead_tube_coral_wall_fan')
    DETECTOR_RAIL = ('detector_rail')
    DIAMOND_BLOCK = ('diamond_block')
    DIAMOND_ORE = ('diamond_ore')
    DIORITE = ('diorite')
    DIORITE_SLAB = ('diorite_slab')
    DIORITE_STAIRS = ('diorite_stairs')
    DIORITE_WALL = ('diorite_wall')
    DIRT = ('dirt')
    DISPENSER = ('dispenser')
    DRAGON_EGG = ('dragon_egg')
    DRAGON_HEAD = ('dragon_head')
    DRAGON_WALL_HEAD = ('dragon_wall_head')
    DRIED_KELP_BLOCK = ('dried_kelp_block')
    DROPPER = ('dropper')
    EMERALD_BLOCK = ('emerald_block')
    EMERALD_ORE = ('emerald_ore')
    ENCHANTING_TABLE = ('enchanting_table')
    ENDER_CHEST = ('ender_chest')
    END_GATEWAY = ('end_gateway')
    END_PORTAL = ('end_portal')
    END_PORTAL_FRAME = ('end_portal_frame')
    END_ROD = ('end_rod')
    END_STONE = ('end_stone')
    END_STONE_BRICKS = ('end_stone_bricks')
    END_STONE_BRICK_SLAB = ('end_stone_brick_slab')
    END_STONE_BRICK_STAIRS = ('end_stone_brick_stairs')
    END_STONE_BRICK_WALL = ('end_stone_brick_wall')
    FARMLAND = ('farmland')
    FERN = ('fern')
    FIRE = ('fire')
    FIRE_CORAL = ('fire_coral')
    FIRE_CORAL_BLOCK = ('fire_coral_block')
    FIRE_CORAL_FAN = ('fire_coral_fan')
    FIRE_CORAL_WALL_FAN = ('fire_coral_wall_fan')
    FLETCHING_TABLE = ('fletching_table')
    FLOWER_POT = ('flower_pot')
    FROSTED_ICE = ('frosted_ice')
    FURNACE = ('furnace')
    GLASS = ('glass')
    GLASS_PANE = ('glass_pane')
    GLOWSTONE = ('glowstone')
    GOLD_BLOCK = ('gold_block')
    GOLD_ORE = ('gold_ore')
    GRANITE = ('granite')
    GRANITE_SLAB = ('granite_slab')
    GRANITE_STAIRS = ('granite_stairs')
    GRANITE_WALL = ('granite_wall')
    GRASS = ('grass')
    GRASS_BLOCK = ('grass_block')
    GRASS_PATH = ('grass_path')
    GRAVEL = ('gravel')
    GRAY_BANNER = ('gray_banner')
    GRAY_BED = ('gray_bed')
    GRAY_CARPET = ('gray_carpet')
    GRAY_CONCRETE = ('gray_concrete')
    GRAY_CONCRETE_POWDER = ('gray_concrete_powder')
    GRAY_GLAZED_TERRACOTTA = ('gray_glazed_terracotta')
    GRAY_SHULKER_BOX = ('gray_shulker_box')
    GRAY_STAINED_GLASS = ('gray_stained_glass')
    GRAY_STAINED_GLASS_PANE = ('gray_stained_glass_pane')
    GRAY_TERRACOTTA = ('gray_terracotta')
    GRAY_WALL_BANNER = ('gray_wall_banner')
    GRAY_WOOL = ('gray_wool')
    GREEN_BANNER = ('green_banner')
    GREEN_BED = ('green_bed')
    GREEN_CARPET = ('green_carpet')
    GREEN_CONCRETE = ('green_concrete')
    GREEN_CONCRETE_POWDER = ('green_concrete_powder')
    GREEN_GLAZED_TERRACOTTA = ('green_glazed_terracotta')
    GREEN_SHULKER_BOX = ('green_shulker_box')
    GREEN_STAINED_GLASS = ('green_stained_glass')
    GREEN_STAINED_GLASS_PANE = ('green_stained_glass_pane')
    GREEN_TERRACOTTA = ('green_terracotta')
    GREEN_WALL_BANNER = ('green_wall_banner')
    GREEN_WOOL = ('green_wool')
    GRINDSTONE = ('grindstone')
    HAY_BLOCK = ('hay_block')
    HEAVY_WEIGHTED_PRESSURE_PLATE = ('heavy_weighted_pressure_plate')
    HONEYCOMB_BLOCK = ('honeycomb_block')
    HONEY_BLOCK = ('honey_block')
    HOPPER = ('hopper')
    HORN_CORAL = ('horn_coral')
    HORN_CORAL_BLOCK = ('horn_coral_block')
    HORN_CORAL_FAN = ('horn_coral_fan')
    HORN_CORAL_WALL_FAN = ('horn_coral_wall_fan')
    ICE = ('ice')
    INFESTED_CHISELED_STONE_BRICKS = ('infested_chiseled_stone_bricks')
    INFESTED_COBBLESTONE = ('infested_cobblestone')
    INFESTED_CRACKED_STONE_BRICKS = ('infested_cracked_stone_bricks')
    INFESTED_MOSSY_STONE_BRICKS = ('infested_mossy_stone_bricks')
    INFESTED_STONE = ('infested_stone')
    INFESTED_STONE_BRICKS = ('infested_stone_bricks')
    IRON_BARS = ('iron_bars')
    IRON_BLOCK = ('iron_block')
    IRON_DOOR = ('iron_door')
    IRON_ORE = ('iron_ore')
    IRON_TRAPDOOR = ('iron_trapdoor')
    JACK_O_LANTERN = ('jack_o_lantern')
    JIGSAW = ('jigsaw')
    JUKEBOX = ('jukebox')
    JUNGLE_BUTTON = ('jungle_button')
    JUNGLE_DOOR = ('jungle_door')
    JUNGLE_FENCE = ('jungle_fence')
    JUNGLE_FENCE_GATE = ('jungle_fence_gate')
    JUNGLE_LEAVES = ('jungle_leaves')
    JUNGLE_LOG = ('jungle_log')
    JUNGLE_PLANKS = ('jungle_planks')
    JUNGLE_PRESSURE_PLATE = ('jungle_pressure_plate')
    JUNGLE_SAPLING = ('jungle_sapling')
    JUNGLE_SIGN = ('jungle_sign')
    JUNGLE_SLAB = ('jungle_slab')
    JUNGLE_STAIRS = ('jungle_stairs')
    JUNGLE_TRAPDOOR = ('jungle_trapdoor')
    JUNGLE_WALL_SIGN = ('jungle_wall_sign')
    JUNGLE_WOOD = ('jungle_wood')
    KELP = ('kelp')
    KELP_PLANT = ('kelp_plant')
    LADDER = ('ladder')
    LANTERN = ('lantern')
    LAPIS_BLOCK = ('lapis_block')
    LAPIS_ORE = ('lapis_ore')
    LARGE_FERN = ('large_fern')
    LAVA = ('lava')
    LECTERN = ('lectern')
    LEVER = ('lever')
    LIGHT_BLUE_BANNER = ('light_blue_banner')
    LIGHT_BLUE_BED = ('light_blue_bed')
    LIGHT_BLUE_CARPET = ('light_blue_carpet')
    LIGHT_BLUE_CONCRETE = ('light_blue_concrete')
    LIGHT_BLUE_CONCRETE_POWDER = ('light_blue_concrete_powder')
    LIGHT_BLUE_GLAZED_TERRACOTTA = ('light_blue_glazed_terracotta')
    LIGHT_BLUE_SHULKER_BOX = ('light_blue_shulker_box')
    LIGHT_BLUE_STAINED_GLASS = ('light_blue_stained_glass')
    LIGHT_BLUE_STAINED_GLASS_PANE = ('light_blue_stained_glass_pane')
    LIGHT_BLUE_TERRACOTTA = ('light_blue_terracotta')
    LIGHT_BLUE_WALL_BANNER = ('light_blue_wall_banner')
    LIGHT_BLUE_WOOL = ('light_blue_wool')
    LIGHT_GRAY_BANNER = ('light_gray_banner')
    LIGHT_GRAY_BED = ('light_gray_bed')
    LIGHT_GRAY_CARPET = ('light_gray_carpet')
    LIGHT_GRAY_CONCRETE = ('light_gray_concrete')
    LIGHT_GRAY_CONCRETE_POWDER = ('light_gray_concrete_powder')
    LIGHT_GRAY_GLAZED_TERRACOTTA = ('light_gray_glazed_terracotta')
    LIGHT_GRAY_SHULKER_BOX = ('light_gray_shulker_box')
    LIGHT_GRAY_STAINED_GLASS = ('light_gray_stained_glass')
    LIGHT_GRAY_STAINED_GLASS_PANE = ('light_gray_stained_glass_pane')
    LIGHT_GRAY_TERRACOTTA = ('light_gray_terracotta')
    LIGHT_GRAY_WALL_BANNER = ('light_gray_wall_banner')
    LIGHT_GRAY_WOOL = ('light_gray_wool')
    LIGHT_WEIGHTED_PRESSURE_PLATE = ('light_weighted_pressure_plate')
    LILAC = ('lilac')
    LILY_OF_THE_VALLEY = ('lily_of_the_valley')
    LILY_PAD = ('lily_pad')
    LIME_BANNER = ('lime_banner')
    LIME_BED = ('lime_bed')
    LIME_CARPET = ('lime_carpet')
    LIME_CONCRETE = ('lime_concrete')
    LIME_CONCRETE_POWDER = ('lime_concrete_powder')
    LIME_GLAZED_TERRACOTTA = ('lime_glazed_terracotta')
    LIME_SHULKER_BOX = ('lime_shulker_box')
    LIME_STAINED_GLASS = ('lime_stained_glass')
    LIME_STAINED_GLASS_PANE = ('lime_stained_glass_pane')
    LIME_TERRACOTTA = ('lime_terracotta')
    LIME_WALL_BANNER = ('lime_wall_banner')
    LIME_WOOL = ('lime_wool')
    LOOM = ('loom')
    MAGENTA_BANNER = ('magenta_banner')
    MAGENTA_BED = ('magenta_bed')
    MAGENTA_CARPET = ('magenta_carpet')
    MAGENTA_CONCRETE = ('magenta_concrete')
    MAGENTA_CONCRETE_POWDER = ('magenta_concrete_powder')
    MAGENTA_GLAZED_TERRACOTTA = ('magenta_glazed_terracotta')
    MAGENTA_SHULKER_BOX = ('magenta_shulker_box')
    MAGENTA_STAINED_GLASS = ('magenta_stained_glass')
    MAGENTA_STAINED_GLASS_PANE = ('magenta_stained_glass_pane')
    MAGENTA_TERRACOTTA = ('magenta_terracotta')
    MAGENTA_WALL_BANNER = ('magenta_wall_banner')
    MAGENTA_WOOL = ('magenta_wool')
    MAGMA_BLOCK = ('magma_block')
    MELON = ('melon')
    MELON_STEM = ('melon_stem')
    MOSSY_COBBLESTONE = ('mossy_cobblestone')
    MOSSY_COBBLESTONE_SLAB = ('mossy_cobblestone_slab')
    MOSSY_COBBLESTONE_STAIRS = ('mossy_cobblestone_stairs')
    MOSSY_COBBLESTONE_WALL = ('mossy_cobblestone_wall')
    MOSSY_STONE_BRICKS = ('mossy_stone_bricks')
    MOSSY_STONE_BRICK_SLAB = ('mossy_stone_brick_slab')
    MOSSY_STONE_BRICK_STAIRS = ('mossy_stone_brick_stairs')
    MOSSY_STONE_BRICK_WALL = ('mossy_stone_brick_wall')
    MOVING_PISTON = ('moving_piston')
    MUSHROOM_STEM = ('mushroom_stem')
    MYCELIUM = ('mycelium')
    NETHERRACK = ('netherrack')
    NETHER_BRICKS = ('nether_bricks')
    NETHER_BRICK_FENCE = ('nether_brick_fence')
    NETHER_BRICK_SLAB = ('nether_brick_slab')
    NETHER_BRICK_STAIRS = ('nether_brick_stairs')
    NETHER_BRICK_WALL = ('nether_brick_wall')
    NETHER_PORTAL = ('nether_portal')
    NETHER_QUARTZ_ORE = ('nether_quartz_ore')
    NETHER_WART = ('nether_wart')
    NETHER_WART_BLOCK = ('nether_wart_block')
    NOTE_BLOCK = ('note_block')
    OAK_BUTTON = ('oak_button')
    OAK_DOOR = ('oak_door')
    OAK_FENCE = ('oak_fence')
    OAK_FENCE_GATE = ('oak_fence_gate')
    OAK_LEAVES = ('oak_leaves')
    OAK_LOG = ('oak_log')
    OAK_PLANKS = ('oak_planks')
    OAK_PRESSURE_PLATE = ('oak_pressure_plate')
    OAK_SAPLING = ('oak_sapling')
    OAK_SIGN = ('oak_sign')
    OAK_SLAB = ('oak_slab')
    OAK_STAIRS = ('oak_stairs')
    OAK_TRAPDOOR = ('oak_trapdoor')
    OAK_WALL_SIGN = ('oak_wall_sign')
    OAK_WOOD = ('oak_wood')
    OBSERVER = ('observer')
    OBSIDIAN = ('obsidian')
    ORANGE_BANNER = ('orange_banner')
    ORANGE_BED = ('orange_bed')
    ORANGE_CARPET = ('orange_carpet')
    ORANGE_CONCRETE = ('orange_concrete')
    ORANGE_CONCRETE_POWDER = ('orange_concrete_powder')
    ORANGE_GLAZED_TERRACOTTA = ('orange_glazed_terracotta')
    ORANGE_SHULKER_BOX = ('orange_shulker_box')
    ORANGE_STAINED_GLASS = ('orange_stained_glass')
    ORANGE_STAINED_GLASS_PANE = ('orange_stained_glass_pane')
    ORANGE_TERRACOTTA = ('orange_terracotta')
    ORANGE_TULIP = ('orange_tulip')
    ORANGE_WALL_BANNER = ('orange_wall_banner')
    ORANGE_WOOL = ('orange_wool')
    OXEYE_DAISY = ('oxeye_daisy')
    PACKED_ICE = ('packed_ice')
    PEONY = ('peony')
    PETRIFIED_OAK_SLAB = ('petrified_oak_slab')
    PINK_BANNER = ('pink_banner')
    PINK_BED = ('pink_bed')
    PINK_CARPET = ('pink_carpet')
    PINK_CONCRETE = ('pink_concrete')
    PINK_CONCRETE_POWDER = ('pink_concrete_powder')
    PINK_GLAZED_TERRACOTTA = ('pink_glazed_terracotta')
    PINK_SHULKER_BOX = ('pink_shulker_box')
    PINK_STAINED_GLASS = ('pink_stained_glass')
    PINK_STAINED_GLASS_PANE = ('pink_stained_glass_pane')
    PINK_TERRACOTTA = ('pink_terracotta')
    PINK_TULIP = ('pink_tulip')
    PINK_WALL_BANNER = ('pink_wall_banner')
    PINK_WOOL = ('pink_wool')
    PISTON = ('piston')
    PISTON_HEAD = ('piston_head')
    PLAYER_HEAD = ('player_head')
    PLAYER_WALL_HEAD = ('player_wall_head')
    PODZOL = ('podzol')
    POLISHED_ANDESITE = ('polished_andesite')
    POLISHED_ANDESITE_SLAB = ('polished_andesite_slab')
    POLISHED_ANDESITE_STAIRS = ('polished_andesite_stairs')
    POLISHED_DIORITE = ('polished_diorite')
    POLISHED_DIORITE_SLAB = ('polished_diorite_slab')
    POLISHED_DIORITE_STAIRS = ('polished_diorite_stairs')
    POLISHED_GRANITE = ('polished_granite')
    POLISHED_GRANITE_SLAB = ('polished_granite_slab')
    POLISHED_GRANITE_STAIRS = ('polished_granite_stairs')
    POPPY = ('poppy')
    POTATOES = ('potatoes')
    POTTED_ACACIA_SAPLING = ('potted_acacia_sapling')
    POTTED_ALLIUM = ('potted_allium')
    POTTED_AZURE_BLUET = ('potted_azure_bluet')
    POTTED_BAMBOO = ('potted_bamboo')
    POTTED_BIRCH_SAPLING = ('potted_birch_sapling')
    POTTED_BLUE_ORCHID = ('potted_blue_orchid')
    POTTED_BROWN_MUSHROOM = ('potted_brown_mushroom')
    POTTED_CACTUS = ('potted_cactus')
    POTTED_CORNFLOWER = ('potted_cornflower')
    POTTED_DANDELION = ('potted_dandelion')
    POTTED_DARK_OAK_SAPLING = ('potted_dark_oak_sapling')
    POTTED_DEAD_BUSH = ('potted_dead_bush')
    POTTED_FERN = ('potted_fern')
    POTTED_JUNGLE_SAPLING = ('potted_jungle_sapling')
    POTTED_LILY_OF_THE_VALLEY = ('potted_lily_of_the_valley')
    POTTED_OAK_SAPLING = ('potted_oak_sapling')
    POTTED_ORANGE_TULIP = ('potted_orange_tulip')
    POTTED_OXEYE_DAISY = ('potted_oxeye_daisy')
    POTTED_PINK_TULIP = ('potted_pink_tulip')
    POTTED_POPPY = ('potted_poppy')
    POTTED_RED_MUSHROOM = ('potted_red_mushroom')
    POTTED_RED_TULIP = ('potted_red_tulip')
    POTTED_SPRUCE_SAPLING = ('potted_spruce_sapling')
    POTTED_WHITE_TULIP = ('potted_white_tulip')
    POTTED_WITHER_ROSE = ('potted_wither_rose')
    POWERED_RAIL = ('powered_rail')
    PRISMARINE = ('prismarine')
    PRISMARINE_BRICKS = ('prismarine_bricks')
    PRISMARINE_BRICK_SLAB = ('prismarine_brick_slab')
    PRISMARINE_BRICK_STAIRS = ('prismarine_brick_stairs')
    PRISMARINE_SLAB = ('prismarine_slab')
    PRISMARINE_STAIRS = ('prismarine_stairs')
    PRISMARINE_WALL = ('prismarine_wall')
    PUMPKIN = ('pumpkin')
    PUMPKIN_STEM = ('pumpkin_stem')
    PURPLE_BANNER = ('purple_banner')
    PURPLE_BED = ('purple_bed')
    PURPLE_CARPET = ('purple_carpet')
    PURPLE_CONCRETE = ('purple_concrete')
    PURPLE_CONCRETE_POWDER = ('purple_concrete_powder')
    PURPLE_GLAZED_TERRACOTTA = ('purple_glazed_terracotta')
    PURPLE_SHULKER_BOX = ('purple_shulker_box')
    PURPLE_STAINED_GLASS = ('purple_stained_glass')
    PURPLE_STAINED_GLASS_PANE = ('purple_stained_glass_pane')
    PURPLE_TERRACOTTA = ('purple_terracotta')
    PURPLE_WALL_BANNER = ('purple_wall_banner')
    PURPLE_WOOL = ('purple_wool')
    PURPUR_BLOCK = ('purpur_block')
    PURPUR_PILLAR = ('purpur_pillar')
    PURPUR_SLAB = ('purpur_slab')
    PURPUR_STAIRS = ('purpur_stairs')
    QUARTZ_BLOCK = ('quartz_block')
    QUARTZ_PILLAR = ('quartz_pillar')
    QUARTZ_SLAB = ('quartz_slab')
    QUARTZ_STAIRS = ('quartz_stairs')
    RAIL = ('rail')
    REDSTONE_BLOCK = ('redstone_block')
    REDSTONE_LAMP = ('redstone_lamp')
    REDSTONE_ORE = ('redstone_ore')
    REDSTONE_TORCH = ('redstone_torch')
    REDSTONE_WALL_TORCH = ('redstone_wall_torch')
    REDSTONE_WIRE = ('redstone_wire')
    RED_BANNER = ('red_banner')
    RED_BED = ('red_bed')
    RED_CARPET = ('red_carpet')
    RED_CONCRETE = ('red_concrete')
    RED_CONCRETE_POWDER = ('red_concrete_powder')
    RED_GLAZED_TERRACOTTA = ('red_glazed_terracotta')
    RED_MUSHROOM = ('red_mushroom')
    RED_MUSHROOM_BLOCK = ('red_mushroom_block')
    RED_NETHER_BRICKS = ('red_nether_bricks')
    RED_NETHER_BRICK_SLAB = ('red_nether_brick_slab')
    RED_NETHER_BRICK_STAIRS = ('red_nether_brick_stairs')
    RED_NETHER_BRICK_WALL = ('red_nether_brick_wall')
    RED_SAND = ('red_sand')
    RED_SANDSTONE = ('red_sandstone')
    RED_SANDSTONE_SLAB = ('red_sandstone_slab')
    RED_SANDSTONE_STAIRS = ('red_sandstone_stairs')
    RED_SANDSTONE_WALL = ('red_sandstone_wall')
    RED_SHULKER_BOX = ('red_shulker_box')
    RED_STAINED_GLASS = ('red_stained_glass')
    RED_STAINED_GLASS_PANE = ('red_stained_glass_pane')
    RED_TERRACOTTA = ('red_terracotta')
    RED_TULIP = ('red_tulip')
    RED_WALL_BANNER = ('red_wall_banner')
    RED_WOOL = ('red_wool')
    REPEATER = ('repeater')
    REPEATING_COMMAND_BLOCK = ('repeating_command_block')
    ROSE_BUSH = ('rose_bush')
    SAND = ('sand')
    SANDSTONE = ('sandstone')
    SANDSTONE_SLAB = ('sandstone_slab')
    SANDSTONE_STAIRS = ('sandstone_stairs')
    SANDSTONE_WALL = ('sandstone_wall')
    SCAFFOLDING = ('scaffolding')
    SEAGRASS = ('seagrass')
    SEA_LANTERN = ('sea_lantern')
    SEA_PICKLE = ('sea_pickle')
    SHULKER_BOX = ('shulker_box')
    SKELETON_SKULL = ('skeleton_skull')
    SKELETON_WALL_SKULL = ('skeleton_wall_skull')
    SLIME_BLOCK = ('slime_block')
    SMITHING_TABLE = ('smithing_table')
    SMOKER = ('smoker')
    SMOOTH_QUARTZ = ('smooth_quartz')
    SMOOTH_QUARTZ_SLAB = ('smooth_quartz_slab')
    SMOOTH_QUARTZ_STAIRS = ('smooth_quartz_stairs')
    SMOOTH_RED_SANDSTONE = ('smooth_red_sandstone')
    SMOOTH_RED_SANDSTONE_SLAB = ('smooth_red_sandstone_slab')
    SMOOTH_RED_SANDSTONE_STAIRS = ('smooth_red_sandstone_stairs')
    SMOOTH_SANDSTONE = ('smooth_sandstone')
    SMOOTH_SANDSTONE_SLAB = ('smooth_sandstone_slab')
    SMOOTH_SANDSTONE_STAIRS = ('smooth_sandstone_stairs')
    SMOOTH_STONE = ('smooth_stone')
    SMOOTH_STONE_SLAB = ('smooth_stone_slab')
    SNOW = ('snow')
    SNOW_BLOCK = ('snow_block')
    SOUL_SAND = ('soul_sand')
    SPAWNER = ('spawner')
    SPONGE = ('sponge')
    SPRUCE_BUTTON = ('spruce_button')
    SPRUCE_DOOR = ('spruce_door')
    SPRUCE_FENCE = ('spruce_fence')
    SPRUCE_FENCE_GATE = ('spruce_fence_gate')
    SPRUCE_LEAVES = ('spruce_leaves')
    SPRUCE_LOG = ('spruce_log')
    SPRUCE_PLANKS = ('spruce_planks')
    SPRUCE_PRESSURE_PLATE = ('spruce_pressure_plate')
    SPRUCE_SAPLING = ('spruce_sapling')
    SPRUCE_SIGN = ('spruce_sign')
    SPRUCE_SLAB = ('spruce_slab')
    SPRUCE_STAIRS = ('spruce_stairs')
    SPRUCE_TRAPDOOR = ('spruce_trapdoor')
    SPRUCE_WALL_SIGN = ('spruce_wall_sign')
    SPRUCE_WOOD = ('spruce_wood')
    STICKY_PISTON = ('sticky_piston')
    STONE = ('stone')
    STONECUTTER = ('stonecutter')
    STONE_BRICKS = ('stone_bricks')
    STONE_BRICK_SLAB = ('stone_brick_slab')
    STONE_BRICK_STAIRS = ('stone_brick_stairs')
    STONE_BRICK_WALL = ('stone_brick_wall')
    STONE_BUTTON = ('stone_button')
    STONE_PRESSURE_PLATE = ('stone_pressure_plate')
    STONE_SLAB = ('stone_slab')
    STONE_STAIRS = ('stone_stairs')
    STRIPPED_ACACIA_LOG = ('stripped_acacia_log')
    STRIPPED_ACACIA_WOOD = ('stripped_acacia_wood')
    STRIPPED_BIRCH_LOG = ('stripped_birch_log')
    STRIPPED_BIRCH_WOOD = ('stripped_birch_wood')
    STRIPPED_DARK_OAK_LOG = ('stripped_dark_oak_log')
    STRIPPED_DARK_OAK_WOOD = ('stripped_dark_oak_wood')
    STRIPPED_JUNGLE_LOG = ('stripped_jungle_log')
    STRIPPED_JUNGLE_WOOD = ('stripped_jungle_wood')
    STRIPPED_OAK_LOG = ('stripped_oak_log')
    STRIPPED_OAK_WOOD = ('stripped_oak_wood')
    STRIPPED_SPRUCE_LOG = ('stripped_spruce_log')
    STRIPPED_SPRUCE_WOOD = ('stripped_spruce_wood')
    STRUCTURE_BLOCK = ('structure_block')
    STRUCTURE_VOID = ('structure_void')
    SUGAR_CANE = ('sugar_cane')
    SUNFLOWER = ('sunflower')
    SWEET_BERRY_BUSH = ('sweet_berry_bush')
    TALL_GRASS = ('tall_grass')
    TALL_SEAGRASS = ('tall_seagrass')
    TERRACOTTA = ('terracotta')
    TNT = ('tnt')
    TORCH = ('torch')
    TRAPPED_CHEST = ('trapped_chest')
    TRIPWIRE = ('tripwire')
    TRIPWIRE_HOOK = ('tripwire_hook')
    TUBE_CORAL = ('tube_coral')
    TUBE_CORAL_BLOCK = ('tube_coral_block')
    TUBE_CORAL_FAN = ('tube_coral_fan')
    TUBE_CORAL_WALL_FAN = ('tube_coral_wall_fan')
    TURTLE_EGG = ('turtle_egg')
    VINE = ('vine')
    VOID_AIR = ('void_air')
    WALL_TORCH = ('wall_torch')
    WATER = ('water')
    WET_SPONGE = ('wet_sponge')
    WHEAT = ('wheat')
    WHITE_BANNER = ('white_banner')
    WHITE_BED = ('white_bed')
    WHITE_CARPET = ('white_carpet')
    WHITE_CONCRETE = ('white_concrete')
    WHITE_CONCRETE_POWDER = ('white_concrete_powder')
    WHITE_GLAZED_TERRACOTTA = ('white_glazed_terracotta')
    WHITE_SHULKER_BOX = ('white_shulker_box')
    WHITE_STAINED_GLASS = ('white_stained_glass')
    WHITE_STAINED_GLASS_PANE = ('white_stained_glass_pane')
    WHITE_TERRACOTTA = ('white_terracotta')
    WHITE_TULIP = ('white_tulip')
    WHITE_WALL_BANNER = ('white_wall_banner')
    WHITE_WOOL = ('white_wool')
    WITHER_ROSE = ('wither_rose')
    WITHER_SKELETON_SKULL = ('wither_skeleton_skull')
    WITHER_SKELETON_WALL_SKULL = ('wither_skeleton_wall_skull')
    YELLOW_BANNER = ('yellow_banner')
    YELLOW_BED = ('yellow_bed')
    YELLOW_CARPET = ('yellow_carpet')
    YELLOW_CONCRETE = ('yellow_concrete')
    YELLOW_CONCRETE_POWDER = ('yellow_concrete_powder')
    YELLOW_GLAZED_TERRACOTTA = ('yellow_glazed_terracotta')
    YELLOW_SHULKER_BOX = ('yellow_shulker_box')
    YELLOW_STAINED_GLASS = ('yellow_stained_glass')
    YELLOW_STAINED_GLASS_PANE = ('yellow_stained_glass_pane')
    YELLOW_TERRACOTTA = ('yellow_terracotta')
    YELLOW_WALL_BANNER = ('yellow_wall_banner')
    YELLOW_WOOL = ('yellow_wool')
    ZOMBIE_HEAD = ('zombie_head')
    ZOMBIE_WALL_HEAD = ('zombie_wall_head')

    # ----------- UTILITY METHODS BELOW ----------
    def is_air(self):
        return bool(self is Material.AIR or self is Material.CAVE_AIR or self is Material.VOID_AIR)
