import astar
import cart
import definitions
import geneticalgorithm
import graph
import image_slicer
import map
import neuralnetwork
import os
import plant
import pygame
import station
import treelearn


def main():
    # inicjowanie pygame'a
    pygame.init()
    pygame.display.set_caption("Smart Cart")
    # tworzenie podstawowych obiektów
    map1 = map.Map([])
    map1.create_base_map()
    move_list = ["rotate_left", "move", "move", "move", "move", "move", "move", "rotate_left", "rotate_left", "move",
                 "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left",
                 "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move",
                 "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left",
                 "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move",
                 "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "move",
                 "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left",
                 "rotate_left", "rotate_left", "move", "move", "rotate_left", "rotate_left", "rotate_left",
                 "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move",
                 "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move",
                 "rotate_left", "rotate_left", "move", "move", "move", "rotate_left", "rotate_left", "rotate_left",
                 "rotate_left", "rotate_left", "move", "move", "rotate_left", "rotate_left", "rotate_left",
                 "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move",
                 "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left",
                 "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left",
                 "move"]  # początkowe ruchy
    amount_of_seeds_dict = {"beetroot": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE,
                            "carrot": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE,
                            "potato": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE,
                            "wheat": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE}
    collected_plants_dict_cart = {"beetroot": 0, "carrot": 0, "potato": 0, "wheat": 0}
    collected_plants_dict_station = {"beetroot": 0, "carrot": 0, "potato": 0, "wheat": 0}
    fertilizer_dict = {"beetroot": definitions.CART_FERTILIZER, "carrot": definitions.CART_FERTILIZER,
                       "potato": definitions.CART_FERTILIZER, "wheat": definitions.CART_FERTILIZER}
    station1 = station.Station(collected_plants_dict_station)
    cart1 = cart.Cart(amount_of_seeds_dict, collected_plants_dict_cart, definitions.CART_DIRECTION_WEST,
                      fertilizer_dict, definitions.CART_FUEL, definitions.CART_WATER_LEVEL, 0 * definitions.BLOCK_SIZE,
                      0 * definitions.BLOCK_SIZE)
    cart1_rect = pygame.Rect(cart1.get_x(), cart1.get_y(), definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
    clock = pygame.time.Clock()
    tree = treelearn.treelearn()  # tworzenie drzewa decyzyjnego
    decision = [0]  # początkowa decyzja o braku powrotu do stacji (0)
    geneticalgorithm.create_genetic_algorithm()  # stworzenie algorytmu genetycznego
    classes, model = neuralnetwork.create_neural_network()  # uczenie sieci neuronowej
    grow_flower_dandelion = False
    random_movement = False
    run = True
    while run:  # pętla główna programu
        clock.tick(definitions.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        map1.draw_window(cart1, cart1_rect, station1)
        if not move_list:  # jeżeli są jakieś ruchy do wykonania w move_list
            grow_flower_dandelion = True
            pygame.image.save(pygame.display.get_surface(),
                              os.path.join('resources/neural_network/tiles/', 'screen.jpg'))  # zrzut obecnego ekranu
            tiles = image_slicer.slice(os.path.join('resources/neural_network/tiles/', 'screen.jpg'),
                                       row=definitions.HEIGHT_AMOUNT + 1, col=definitions.WIDTH_AMOUNT,
                                       save=False)  # pocięcie ekranu na sto części
            image_slicer.save_tiles(tiles, directory=os.path.join('resources/neural_network/tiles/'), prefix='tile',
                                    format='png')  # zapisanie części do folderu tiles
            os.remove('resources/neural_network/tiles/screen.jpg')
            for char in range(0, definitions.WIDTH_AMOUNT):
                if str(char) == "0":
                    os.remove('resources/neural_network/tiles/tile_11_10.png')
                else:
                    os.remove('resources/neural_network/tiles/tile_11_0' + str(char) + '.png')
            istate = graph.Istate(cart1.get_direction(), cart1.get_x() / definitions.BLOCK_SIZE,
                                  cart1.get_y() / definitions.BLOCK_SIZE)  # stan początkowy wózka (jego orientacja oraz jego aktualne miejsce)
            if neuralnetwork.predfield(classes, istate, model) is not False:  # jeżeli istnieje jakaś dojrzała roślina
                random_movement = False
                if decision == [0]:  # jeżeli decyzja jest 0 (brak powrotu do stacji) to uprawiaj pole
                    move_list = (
                        astar.graphsearch([], astar.f, [], neuralnetwork.predfield(classes, istate, model), istate,
                                          map1, graph.succ))  # lista z ruchami, które należy po kolei wykonać, astar
                else:  # jeżeli decyzja jest 1 (powrót do stacji) to wróć do stacji uzupełnić zapasy
                    move_list = (graph.graphsearch([], [], (0, 0), istate,
                                                   graph.succ))  # lista z ruchami, które należy po kolei wykonać, graphsearch
            else:
                random_movement = True
        elif move_list:  # jeżeli move_list nie jest pusta
            cart1.handle_movement(cart1_rect,
                                  move_list.pop(0))  # wykonaj kolejny ruch oraz zdejmij ten ruch z początku listy
        if random_movement is True:
            cart1.handle_movement_random(cart1_rect)  # wykonuj losowe ruchy
        cart1.do_work(cart1_rect, map1, station1)  # wykonaj pracę na danym polu
        decision = treelearn.make_decision(cart1.get_all_amount_of_seeds(), cart1.get_all_collected_plants(),
                                           cart1.get_all_fertilizer(), cart1.get_fuel(), tree,
                                           cart1.get_water_level())  # podejmij decyzję czy wracać do stacji (0 : NIE, 1 : TAK)
        if grow_flower_dandelion is True:
            plant.Plant.grow_flower_dandelion(map1)  # losuj urośnięcie kwiatka dandeliona
        plant.Plant.grow_plants(map1)  # zwiększ poziom dojrzałości roślin
    pygame.quit()


if __name__ == "__main__":
    main()
