import os
import pygame
BLOCK_SIZE = 100
DIRT = pygame.image.load(os.path.join('resources', 'dirt.png'))
DIRT = pygame.transform.scale(DIRT, (BLOCK_SIZE, BLOCK_SIZE))
FPS = 1
MAXIMUM_WATER_LEVEL = 100
WHITE = ((255, 255, 255))
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TRACTOR = pygame.image.load(os.path.join('resources', 'tractor.png'))
TRACTOR_WIDTH, TRACTOR_HEIGHT = 100, 100
TRACTOR = pygame.transform.scale(TRACTOR, (TRACTOR_WIDTH, TRACTOR_HEIGHT))
VEL = 100
WHEAT_MAXIMUM_STATE = 5
WHEAT_REQUIRED_WATER_LEVEL = 40
FARMLAND = pygame.image.load(os.path.join('resources', 'farmland.png'))
FARMLAND = pygame.transform.scale(DIRT, (BLOCK_SIZE, BLOCK_SIZE))