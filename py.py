import definitions
import field
import plant
import pygame
import random
import soil
import tractor
pygame.display.set_caption("Smart Tractor")
fields = []
def create_base_map():
    for i in range(10):
        temp_map_field = []
        for j in range(10):
            temp_rect = pygame.Rect(i * definitions.BLOCK_SIZE, j * definitions.BLOCK_SIZE, definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
            temp_soil = soil.Soil(False, False)
            temp_plant = plant.Plant(0, definitions.WHEAT_MAXIMUM_STATE)
            temp_field = field.Field(temp_plant, temp_rect, temp_soil)
            temp_map_field.append(temp_field)
        fields.append(temp_map_field)
def fill_map():
    for i in range(10):
        for j in range(10):
            field = fields[i][j]
            rect = field.get_rect()
            if field.get_soil().get_state() == False:
                block = definitions.DIRT
            definitions.WIN.blit(block, (rect.x, rect.y))
def draw_window(tractor1_rectangle):
    fill_map()
    definitions.WIN.blit(definitions.TRACTOR, (tractor1_rectangle.x, tractor1_rectangle.y))
    pygame.display.update()
def is_move_allowed(move, tractor1_rectangle):
    if ((move == 1) and (tractor1_rectangle.y + definitions.VEL + definitions.BLOCK_SIZE <= definitions.HEIGHT)):
        return True
    elif ((move == 2) and (tractor1_rectangle.x - definitions.VEL >= 0)):
        return True
    elif ((move == 3) and (tractor1_rectangle.x + definitions.VEL + definitions.BLOCK_SIZE <= definitions.WIDTH)):
        return True
    elif ((move == 4) and (tractor1_rectangle.y - definitions.VEL >= 0)):
        return True
    else:
        return False
def tractor1_handle_movement(tractor1, tractor1_rectangle):
    random1 = random.randint(1, 4)
    if ((random1 == 1) and (is_move_allowed(1, tractor1_rectangle) == True)):
        tractor1.move_down()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
    elif ((random1 == 2) and (is_move_allowed(2, tractor1_rectangle) == True)):
        tractor1.move_left()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
    elif ((random1 == 3) and (is_move_allowed(3, tractor1_rectangle) == True)):
        tractor1.move_right()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
    elif ((random1 == 4) and (is_move_allowed(4, tractor1_rectangle) == True)):
        tractor1.move_up()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
def main():
    create_base_map()
    tractor1 = tractor.Tractor(400, 400)
    tractor1_rectangle = pygame.Rect(tractor1.get_x(), tractor1.get_y(), definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(definitions.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        tractor1_handle_movement(tractor1, tractor1_rectangle)
        draw_window(tractor1_rectangle)
    pygame.quit()
if __name__ == "__main__":
    main()