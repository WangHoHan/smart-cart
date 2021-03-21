import os
import pygame
BLOCK_SIZE = 100
DIRT = pygame.image.load(os.path.join('resources', 'dirt.png'))
DIRT = pygame.transform.scale(DIRT, (BLOCK_SIZE, BLOCK_SIZE))
FARMLAND = pygame.image.load(os.path.join('resources', 'farmland.png'))
FARMLAND = pygame.transform.scale(FARMLAND, (BLOCK_SIZE, BLOCK_SIZE))
FPS = 1
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TRACTOR = pygame.image.load(os.path.join('resources', 'tractor.png'))
TRACTOR = pygame.transform.scale(TRACTOR, (BLOCK_SIZE, BLOCK_SIZE))
VEL = 100
WHEAT_MAXIMUM_STATE = 5