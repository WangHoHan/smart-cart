import os
import pygame
FPS = 1
WHITE = ((255, 255, 255))
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TRACTOR = pygame.image.load(os.path.join('resources', 'tractor.png'))
TRACTOR_WIDTH, TRACTOR_HEIGHT = 100, 100
TRACTOR = pygame.transform.scale(TRACTOR, (TRACTOR_WIDTH, TRACTOR_HEIGHT))
VEL = 100