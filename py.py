import os
import pygame
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Tractor")
WHITE = ((255, 255, 255))
FPS = 13
TRACTOR_WIDTH, TRACTOR_HEIGHT = 100, 100
TRACTOR = pygame.image.load(os.path.join('resources', 'tractor.png'))
TRACTOR = pygame.transform.scale(TRACTOR, (TRACTOR_WIDTH, TRACTOR_HEIGHT))
VEL = 100
def draw_window(tractor_rectangle):
    WIN.fill(WHITE)
    WIN.blit(TRACTOR, (tractor_rectangle.x, tractor_rectangle.y))
    pygame.display.update()
def tractor_handle_movement(keys_pressed, tractor_rectangle):
    if keys_pressed[pygame.K_DOWN] and tractor_rectangle.y + VEL + TRACTOR_HEIGHT <= HEIGHT:
        tractor_rectangle.y += VEL
    if keys_pressed[pygame.K_LEFT] and tractor_rectangle.x - VEL >= 0:
        tractor_rectangle.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and tractor_rectangle.x + VEL + TRACTOR_WIDTH <= WIDTH:
        tractor_rectangle.x += VEL
    if keys_pressed[pygame.K_UP] and tractor_rectangle.y - VEL >= 0:
        tractor_rectangle.y -= VEL
def main():
    tractor_rectangle = pygame.Rect(0, 0, TRACTOR_WIDTH, TRACTOR_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        tractor_handle_movement(keys_pressed, tractor_rectangle)
        draw_window(tractor_rectangle)
    pygame.quit()
if __name__ == "__main__":
    main()