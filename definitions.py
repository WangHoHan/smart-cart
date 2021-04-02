import os
import pygame
BLOCK_SIZE = 60
BEETROOTS_GROW_TIME = 5
BEETROOTS_MAXIMUM_STATE = BEETROOTS_GROW_TIME * 3 + 1
BEETROOTS_STAGE_0 = pygame.image.load(os.path.join('resources', 'beetroots_stage_0.png'))
BEETROOTS_STAGE_0 = pygame.transform.scale(BEETROOTS_STAGE_0, (BLOCK_SIZE, BLOCK_SIZE))
BEETROOTS_STAGE_1 = pygame.image.load(os.path.join('resources', 'beetroots_stage_1.png'))
BEETROOTS_STAGE_1 = pygame.transform.scale(BEETROOTS_STAGE_1, (BLOCK_SIZE, BLOCK_SIZE))
BEETROOTS_STAGE_2 = pygame.image.load(os.path.join('resources', 'beetroots_stage_2.png'))
BEETROOTS_STAGE_2 = pygame.transform.scale(BEETROOTS_STAGE_2, (BLOCK_SIZE, BLOCK_SIZE))
BEETROOTS_STAGE_3 = pygame.image.load(os.path.join('resources', 'beetroots_stage_3.png'))
BEETROOTS_STAGE_3 = pygame.transform.scale(BEETROOTS_STAGE_3, (BLOCK_SIZE, BLOCK_SIZE))
CARROTS_GROW_TIME = 5
CARROTS_MAXIMUM_STATE = CARROTS_GROW_TIME * 3 + 1
CARROTS_STAGE_0 = pygame.image.load(os.path.join('resources', 'carrots_stage_0.png'))
CARROTS_STAGE_0 = pygame.transform.scale(CARROTS_STAGE_0, (BLOCK_SIZE, BLOCK_SIZE))
CARROTS_STAGE_1 = pygame.image.load(os.path.join('resources', 'carrots_stage_1.png'))
CARROTS_STAGE_1 = pygame.transform.scale(CARROTS_STAGE_1, (BLOCK_SIZE, BLOCK_SIZE))
CARROTS_STAGE_2 = pygame.image.load(os.path.join('resources', 'carrots_stage_2.png'))
CARROTS_STAGE_2 = pygame.transform.scale(CARROTS_STAGE_2, (BLOCK_SIZE, BLOCK_SIZE))
CARROTS_STAGE_3 = pygame.image.load(os.path.join('resources', 'carrots_stage_3.png'))
CARROTS_STAGE_3 = pygame.transform.scale(CARROTS_STAGE_3, (BLOCK_SIZE, BLOCK_SIZE))
DIRT = pygame.image.load(os.path.join('resources', 'dirt.png'))
DIRT = pygame.transform.scale(DIRT, (BLOCK_SIZE, BLOCK_SIZE))
HEIGHT_AMOUNT, WIDTH_AMOUNT = 10, 10
HEIGHT,  WIDTH = BLOCK_SIZE * HEIGHT_AMOUNT, BLOCK_SIZE * WIDTH_AMOUNT
FARMLAND_DRY = pygame.image.load(os.path.join('resources', 'farmland_dry.png'))
FARMLAND_DRY = pygame.transform.scale(FARMLAND_DRY, (BLOCK_SIZE, BLOCK_SIZE))
FARMLAND_WET = pygame.image.load(os.path.join('resources', 'farmland_wet.png'))
FARMLAND_WET = pygame.transform.scale(FARMLAND_WET, (BLOCK_SIZE, BLOCK_SIZE))
FPS = 1
POTATOES_GROW_TIME = 5
POTATOES_MAXIMUM_STATE = POTATOES_GROW_TIME * 3 + 1
POTATOES_STAGE_0 = pygame.image.load(os.path.join('resources', 'potatoes_stage_0.png'))
POTATOES_STAGE_0 = pygame.transform.scale(POTATOES_STAGE_0, (BLOCK_SIZE, BLOCK_SIZE))
POTATOES_STAGE_1 = pygame.image.load(os.path.join('resources', 'potatoes_stage_1.png'))
POTATOES_STAGE_1 = pygame.transform.scale(POTATOES_STAGE_1, (BLOCK_SIZE, BLOCK_SIZE))
POTATOES_STAGE_2 = pygame.image.load(os.path.join('resources', 'potatoes_stage_2.png'))
POTATOES_STAGE_2 = pygame.transform.scale(POTATOES_STAGE_2, (BLOCK_SIZE, BLOCK_SIZE))
POTATOES_STAGE_3 = pygame.image.load(os.path.join('resources', 'potatoes_stage_3.png'))
POTATOES_STAGE_3 = pygame.transform.scale(POTATOES_STAGE_3, (BLOCK_SIZE, BLOCK_SIZE))
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TRACTOR = pygame.image.load(os.path.join('resources', 'minecart_command_block.png'))
TRACTOR = pygame.transform.scale(TRACTOR, (BLOCK_SIZE, BLOCK_SIZE))
TRACTOR_FERTILIZER = 2
TRACTOR_FUEL = 200
TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE = 20
TRACTOR_MAXIMUM_COLLECTED_PLANTS = 80
TRACTOR_WATER_LEVEL = 40
WHEAT_GROW_TIME = 5
WHEAT_MAXIMUM_STATE = WHEAT_GROW_TIME * 7 + 1
WHEAT_STAGE_0 = pygame.image.load(os.path.join('resources', 'wheat_stage_0.png'))
WHEAT_STAGE_0 = pygame.transform.scale(WHEAT_STAGE_0, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_STAGE_1 = pygame.image.load(os.path.join('resources', 'wheat_stage_1.png'))
WHEAT_STAGE_1 = pygame.transform.scale(WHEAT_STAGE_1, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_STAGE_2 = pygame.image.load(os.path.join('resources', 'wheat_stage_2.png'))
WHEAT_STAGE_2 = pygame.transform.scale(WHEAT_STAGE_2, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_STAGE_3 = pygame.image.load(os.path.join('resources', 'wheat_stage_3.png'))
WHEAT_STAGE_3 = pygame.transform.scale(WHEAT_STAGE_3, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_STAGE_4 = pygame.image.load(os.path.join('resources', 'wheat_stage_4.png'))
WHEAT_STAGE_4 = pygame.transform.scale(WHEAT_STAGE_4, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_STAGE_5 = pygame.image.load(os.path.join('resources', 'wheat_stage_5.png'))
WHEAT_STAGE_5 = pygame.transform.scale(WHEAT_STAGE_5, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_STAGE_6 = pygame.image.load(os.path.join('resources', 'wheat_stage_6.png'))
WHEAT_STAGE_6 = pygame.transform.scale(WHEAT_STAGE_6, (BLOCK_SIZE, BLOCK_SIZE))
WHEAT_STAGE_7 = pygame.image.load(os.path.join('resources', 'wheat_stage_7.png'))
WHEAT_STAGE_7 = pygame.transform.scale(WHEAT_STAGE_7, (BLOCK_SIZE, BLOCK_SIZE))