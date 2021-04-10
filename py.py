import definitions
import graph
import map
import plant
import pygame
import random
import station
import tractor
pygame.display.set_caption("Smart Tractor")
def main():
    #tworzenie podstawowych obiektów
    map1 = map.Map([])
    map1.create_base_map()
    move_list = []
    amount_of_seeds_dict = {"beetroot": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE, "carrot": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE, "potato": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE, "wheat": definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE}
    collected_plants_dict = {"beetroot": 0, "carrot": 0, "potato": 0, "wheat": 0}
    fertilizer_dict = {"beetroot": definitions.TRACTOR_FERTILIZER, "carrot": definitions.TRACTOR_FERTILIZER, "potato": definitions.TRACTOR_FERTILIZER, "wheat": definitions.TRACTOR_FERTILIZER}
    station1 = station.Station(collected_plants_dict)
    tractor1 = tractor.Tractor(amount_of_seeds_dict, collected_plants_dict, definitions.TRACTOR_DIRECTION_SOUTH, fertilizer_dict, definitions.TRACTOR_FUEL, definitions.TRACTOR_WATER_LEVEL, 0, 0)
    tractor1_rect = pygame.Rect(tractor1.get_x(), tractor1.get_y(), definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
    clock = pygame.time.Clock()
    run = True
    while run: #pętla główna programu
        clock.tick(definitions.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        map1.draw_window(tractor1, tractor1_rect)
        if not move_list:
            istate = graph.Istate(tractor1.get_direction(), tractor1.get_x() / definitions.BLOCK_SIZE, tractor1.get_y() / definitions.BLOCK_SIZE)
            r1 = random.randint(1, 9)
            r2 = random.randint(1, 9)
            print(r1)
            print(r2)
            move_list = (graph.graphsearch([], [], istate, graph.succ, (r1, r2)))
            print(move_list)
        elif move_list:
            temp = move_list.pop(0)
            print(temp)
            tractor1.handle_movement(temp, tractor1_rect)
        else:
            tractor1.handle_random_movement(tractor1_rect)
        tractor1.do_work(map1, station1, tractor1_rect)
        plant.Plant.grow_plants(map1)
    pygame.quit()
if __name__ == "__main__":
    main()