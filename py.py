import astar
import definitions
import graph
import map
import plant
import pygame
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
    tractor1 = tractor.Tractor(amount_of_seeds_dict, collected_plants_dict, definitions.TRACTOR_DIRECTION_NORTH, fertilizer_dict, definitions.TRACTOR_FUEL, definitions.TRACTOR_WATER_LEVEL, 0, 0)
    tractor1_rect = pygame.Rect(tractor1.get_x(), tractor1.get_y(), definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
    clock = pygame.time.Clock()
    run = True
    while run: #pętla główna programu
        clock.tick(definitions.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        map1.draw_window(tractor1, tractor1_rect)
        if not move_list and plant.Plant.if_any_mature_plant(map1) is True: #jeżeli są jakieś ruchy do wykonania w move_list oraz istnieje jakaś dojrzała roślina
            istate = graph.Istate(tractor1.get_direction(), tractor1.get_x() / definitions.BLOCK_SIZE, tractor1.get_y() / definitions.BLOCK_SIZE) #stan początkowy traktora (jego orientacja oraz jego aktualne współrzędne)
            #move_list = (graph.graphsearch([], [], istate, graph.succ, plant.Plant.get_closest_mature_plant(map1, tractor1))) #lista z ruchami, które należy po kolei wykonać, graph
            move_list = (astar.graphsearch([], [], istate, graph.succ, plant.Plant.get_closest_mature_plant(map1, istate), astar.f, map1)) #lista z ruchami, które należy po kolei wykonać, astar
        elif move_list: #jeżeli move_list nie jest pusta
            tractor1.handle_movement(move_list.pop(0), tractor1_rect) #wykonaj kolejny ruch oraz zdejmij ten ruch z początku listy
        else:
            tractor1.handle_random_movement(tractor1_rect) #wykonuj losowe ruchy
        tractor1.do_work(map1, station1, tractor1_rect) #wykonaj pracę na danym polu
        plant.Plant.grow_plants(map1) #zwiększ poziom dojrzałości roślin
    pygame.quit()
if __name__ == "__main__":
    main()