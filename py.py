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
            temp_soil = soil.Soil(False, False, False)
            temp_plant = plant.Plant("none", 0)
            temp_field = field.Field(temp_plant, temp_rect, temp_soil)
            temp_map_field.append(temp_field)
        fields.append(temp_map_field)
def fill_map():
    for i in range(10):
        for j in range(10):
            field = fields[i][j]
            rect = field.get_rect()
            if field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.BEETROOTS_GROW_TIME:
                block = definitions.BEETROOTSTAGE1
            elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 1 * definitions.BEETROOTS_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.BEETROOTS_GROW_TIME:
                block = definitions.BEETROOTSTAGE2
            elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 2 * definitions.BEETROOTS_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.BEETROOTS_GROW_TIME:
                block = definitions.BEETROOTSTAGE3
            elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() == 3 *definitions.BEETROOTS_GROW_TIME + 1:
                block = definitions.BEETROOTSTAGE4
            elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.CARROTS_GROW_TIME:
                block = definitions.CARROTSTAGE1
            elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 1 * definitions.CARROTS_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.CARROTS_GROW_TIME:
                block = definitions.CARROTSTAGE2
            elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 2 * definitions.CARROTS_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.CARROTS_GROW_TIME:
                block = definitions.CARROTSTAGE3
            elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() == 3 *definitions.CARROTS_GROW_TIME + 1:
                block = definitions.CARROTSTAGE4
            elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.POTATOES_GROW_TIME:
                block = definitions.POTATOSTAGE1
            elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 1 * definitions.POTATOES_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.POTATOES_GROW_TIME:
                block = definitions.POTATOSTAGE2
            elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 2 * definitions.POTATOES_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.POTATOES_GROW_TIME:
                block = definitions.POTATOSTAGE3
            elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() == 3 *definitions.POTATOES_GROW_TIME + 1:
                block = definitions.POTATOSTAGE4
            elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.WHEAT_GROW_TIME:
                block = definitions.WHEATSTAGE1
            elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 1 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.WHEAT_GROW_TIME:
                block = definitions.WHEATSTAGE2
            elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 2 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.WHEAT_GROW_TIME:
                block = definitions.WHEATSTAGE3
            elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 3 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 4 * definitions.WHEAT_GROW_TIME:
                block = definitions.WHEATSTAGE4
            elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() == 4 *definitions.WHEAT_GROW_TIME + 1:
                block = definitions.WHEATSTAGE5
            elif field.get_soil().get_state() is False:
                block = definitions.DIRT
            elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is False:
                block = definitions.FARMLAND
            elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is True:
                block = definitions.FARMLANDMOIST
            definitions.WIN.blit(block, (rect.x, rect.y))
def do_work(tractor1, tractor1_rect):
    loop = True
    if tractor1.get_all_amount_of_seeds() == 0:
        loop = False
    x = int(tractor1_rect.x/100)
    y = int(tractor1_rect.y/100)
    field = fields[x][y]
    if field.get_soil().get_state() is False:
        field.get_soil().set_state(True)
    elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is False and tractor1.get_water_level() > 0:
        tractor1.set_water_level(tractor1.get_water_level() - 1)
        field.get_soil().set_water_level(True)
    elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is True and field.get_plant().get_state() == 0:
        while loop is True:
            random1 = random.randint(1, 4)
            if random1 == 1 and tractor1.get_amount_of_seeds("beetroot") > 0:
                tractor1.set_amount_of_seeds("beetroot", tractor1.get_amount_of_seeds("beetroot") - 1)
                field.get_plant().set_name("beetroot")
                field.get_plant().set_state(1)
                loop = False
            elif random1 == 2 and tractor1.get_amount_of_seeds("carrot") > 0:
                tractor1.set_amount_of_seeds("carrot", tractor1.get_amount_of_seeds("carrot") - 1)
                field.get_plant().set_name("carrot")
                field.get_plant().set_state(1)
                loop = False
            elif random1 == 3 and tractor1.get_amount_of_seeds("potato") > 0:
                tractor1.set_amount_of_seeds("potato", tractor1.get_amount_of_seeds("potato") - 1)
                field.get_plant().set_name("potato")
                field.get_plant().set_state(1)
                loop = False
            elif random1 == 4 and tractor1.get_amount_of_seeds("wheat") > 0:
                tractor1.set_amount_of_seeds("wheat", tractor1.get_amount_of_seeds("wheat") - 1)
                field.get_plant().set_name("wheat")
                field.get_plant().set_state(1)
                loop = False
    elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.BEETROOTS_MAXIMUM_STATE - definitions.BEETROOTS_GROW_TIME and tractor1.get_fertilizer("beetroot") > 0 and field.get_soil().get_is_fertilized() is False:
        tractor1.set_fertilizer("beetroot", (tractor1.get_fertilizer("beetroot") - 1))
        field.get_soil().set_is_fertilized(True)
        field.get_plant().set_state(field.get_plant().get_state() + definitions.BEETROOTS_GROW_TIME)
    elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.CARROTS_MAXIMUM_STATE - definitions.CARROTS_GROW_TIME and tractor1.get_fertilizer("carrot") > 0 and field.get_soil().get_is_fertilized() is False:
        tractor1.set_fertilizer("carrot", (tractor1.get_fertilizer("carrot") - 1))
        field.get_soil().set_is_fertilized(True)
        field.get_plant().set_state(field.get_plant().get_state() + definitions.CARROTS_GROW_TIME)
    elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.POTATOES_MAXIMUM_STATE - definitions.POTATOES_GROW_TIME and tractor1.get_fertilizer("potato") > 0 and field.get_soil().get_is_fertilized() is False:
        tractor1.set_fertilizer("potato", (tractor1.get_fertilizer("potato") - 1))
        field.get_soil().set_is_fertilized(True)
        field.get_plant().set_state(field.get_plant().get_state() + definitions.POTATOES_GROW_TIME)
    elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.WHEAT_MAXIMUM_STATE - definitions.WHEAT_GROW_TIME and tractor1.get_fertilizer("wheat") > 0 and field.get_soil().get_is_fertilized() is False:
        tractor1.set_fertilizer("wheat", (tractor1.get_fertilizer("wheat") - 1))
        field.get_soil().set_is_fertilized(True)
        field.get_plant().set_state(field.get_plant().get_state() + definitions.WHEAT_GROW_TIME)
    elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() == definitions.BEETROOTS_MAXIMUM_STATE and tractor1.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
        field.get_plant().set_state(0)
        field.get_soil().set_is_fertilized(False)
        field.get_soil().set_water_level(False)
        field.get_soil().set_state(False)
        tractor1.set_collected_plants("beetroot", tractor1.get_collected_plants("beetroot") + 1)
    elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() == definitions.CARROTS_MAXIMUM_STATE and tractor1.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
        field.get_plant().set_state(0)
        field.get_soil().set_is_fertilized(False)
        field.get_soil().set_water_level(False)
        field.get_soil().set_state(False)
        tractor1.set_collected_plants("carrot", tractor1.get_collected_plants("carrot") + 1)
    elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() == definitions.POTATOES_MAXIMUM_STATE and tractor1.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
        field.get_plant().set_state(0)
        field.get_soil().set_is_fertilized(False)
        field.get_soil().set_water_level(False)
        field.get_soil().set_state(False)
        tractor1.set_collected_plants("potato", tractor1.get_collected_plants("potato") + 1)
    elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() == definitions.WHEAT_MAXIMUM_STATE and tractor1.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
        field.get_plant().set_state(0)
        field.get_soil().set_is_fertilized(False)
        field.get_soil().set_water_level(False)
        field.get_soil().set_state(False)
        tractor1.set_collected_plants("wheat", tractor1.get_collected_plants("wheat") + 1)
def draw_window(tractor1_rect):
    fill_map()
    definitions.WIN.blit(definitions.TRACTOR, (tractor1_rect.x, tractor1_rect.y))
    pygame.display.update()
def grow_plants():
    for i in range(10):
        for j in range(10):
            field = fields[i][j]
            if field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.BEETROOTS_MAXIMUM_STATE:
                field.get_plant().set_state(field.get_plant().get_state() + 1)
            elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.CARROTS_MAXIMUM_STATE:
                field.get_plant().set_state(field.get_plant().get_state() + 1)
            elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.POTATOES_MAXIMUM_STATE:
                field.get_plant().set_state(field.get_plant().get_state() + 1)
            elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.WHEAT_MAXIMUM_STATE:
                field.get_plant().set_state(field.get_plant().get_state() + 1)
def is_move_allowed(move, tractor1_rect):
    if move == 1 and tractor1_rect.y + definitions.BLOCK_SIZE + definitions.BLOCK_SIZE <= definitions.HEIGHT:
        return True
    elif move == 2 and tractor1_rect.x - definitions.BLOCK_SIZE >= 0:
        return True
    elif move == 3 and tractor1_rect.x + definitions.BLOCK_SIZE + definitions.BLOCK_SIZE <= definitions.WIDTH:
        return True
    elif move == 4 and tractor1_rect.y - definitions.BLOCK_SIZE >= 0:
        return True
    else:
        return False
def tractor1_handle_movement(tractor1, tractor1_rect):
    loop = True
    while loop and tractor1.get_fuel() > 0:
        random1 = random.randint(1, 4)
        if random1 == 1 and is_move_allowed(1, tractor1_rect) is True:
            tractor1.move_down()
            tractor1_rect.x = tractor1.get_x()
            tractor1_rect.y = tractor1.get_y()
            loop = False
        elif random1 == 2 and is_move_allowed(2, tractor1_rect) is True:
            tractor1.move_left()
            tractor1_rect.x = tractor1.get_x()
            tractor1_rect.y = tractor1.get_y()
            loop = False
        elif random1 == 3 and is_move_allowed(3, tractor1_rect) is True:
            tractor1.move_right()
            tractor1_rect.x = tractor1.get_x()
            tractor1_rect.y = tractor1.get_y()
            loop = False
        elif random1 == 4 and is_move_allowed(4, tractor1_rect) is True:
            tractor1.move_up()
            tractor1_rect.x = tractor1.get_x()
            tractor1_rect.y = tractor1.get_y()
            loop = False
    tractor1.set_fuel(tractor1.get_fuel() - 1)
    if tractor1_rect.x == 0 and tractor1_rect.y == 0:
        tractor1.set_fuel(definitions.TRACTOR_FUEL)
        tractor1.set_water_level(definitions.TRACTOR_WATER_LEVEL)
def main():
    create_base_map()
    amount_of_seeds_dict = {"beetroot": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE, "carrot": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE, "potato": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE, "wheat": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE}
    collected_plants_dict = {"beetroot": 0, "carrot": 0, "potato": 0, "wheat": 0}
    fertilizer_dict = {"beetroot": definitions.TRACTOR_FERTILIZER, "carrot": definitions.TRACTOR_FERTILIZER, "potato": definitions.TRACTOR_FERTILIZER, "wheat": definitions.TRACTOR_FERTILIZER}
    tractor1 = tractor.Tractor(amount_of_seeds_dict, collected_plants_dict, fertilizer_dict, definitions.TRACTOR_FUEL, definitions.TRACTOR_WATER_LEVEL ,0, 0)
    tractor1_rect = pygame.Rect(tractor1.get_x(), tractor1.get_y(), definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(definitions.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(tractor1_rect)
        grow_plants()
        tractor1_handle_movement(tractor1, tractor1_rect)
        do_work(tractor1, tractor1_rect)
    pygame.quit()
if __name__ == "__main__":
    main()