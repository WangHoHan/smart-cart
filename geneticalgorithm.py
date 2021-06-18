import astar
import cart
import definitions
import graph
import map
import os
import pickle
import plant
import pygame
import random
import station
import treelearn
def create_genetic_algorithm():
    if os.path.exists("resources/genetic_algorithm/optimalastar.pkl"): #jeżeli algorytm genetyczny utworzył plik wcześcniej to odczytaj
        astar_costs = pickle.load(open(os.path.join('resources/genetic_algorithm', "optimalastar.pkl"), "rb"))
        #kolejność alfabetyczna
        definitions.BEETROOTS_ADULT_COST = astar_costs[0]
        definitions.BEETROOTS_GROW_COST = astar_costs[1]
        definitions.CARROTS_ADULT_COST = astar_costs[2]
        definitions.CARROTS_GROW_COST = astar_costs[3]
        definitions.DIRT_COST = astar_costs[4]
        definitions.FARMLAND_DRY_COST = astar_costs[5]
        definitions.FARMLAND_WET_COST = astar_costs[6]
        definitions.FLOWER_DANDELION_COST = astar_costs[7]
        definitions.POTATOES_ADULT_COST = astar_costs[8]
        definitions.POTATOES_GROW_COST = astar_costs[9]
        definitions.STATION_COST = astar_costs[10]
        definitions.WHEAT_ADULT_COST = astar_costs[11]
        definitions.WHEAT_GROW_COST = astar_costs[12]
    else: #w przeciwnym razie ucz algorytmem genetycznym
        astar_costs = [definitions.BEETROOTS_ADULT_COST, definitions.BEETROOTS_GROW_COST, definitions.CARROTS_ADULT_COST, definitions.CARROTS_GROW_COST, definitions.DIRT_COST, definitions.FARMLAND_DRY_COST, definitions.FARMLAND_WET_COST, definitions.FLOWER_DANDELION_COST, definitions.POTATOES_ADULT_COST, definitions.POTATOES_GROW_COST, definitions.STATION_COST, definitions.WHEAT_ADULT_COST, definitions.WHEAT_GROW_COST] #kolejność alfabetyczna
        astar_costs = evolve(astar_costs)
        pickle.dump(astar_costs, open(os.path.join('resources/genetic_algorithm', "optimalastar.pkl"), "wb"))
def evolve(astar_costs):
    first_generation = [] #pierwsza generacja
    overall_solutions = [] #rozwiązania końcowe
    solutions = [] #rozwiązania danej generacji
    for individual in range(definitions.GENETIC_ALGORITHM_NUMBER_OF_INDIVIDUALS_ZERO): #liczba osobników pierwszej generacji
        for _ in range(definitions.GENETIC_ALGORITHM_COSTS_AMOUNT):
            first_generation.append(random.uniform(0, 10))
        solutions.append(first_generation) #generowanie losowych kosztów pól dla pierwszej generacji
    for gen in range(definitions.GENETIC_ALGORITHM_NUMBER_OF_GENERATIONS): #liczba generacji
        print(f"=== Generation {gen + 1}  ===")
        ranked_solutions = [] #rozwiązania z wynikiem
        index = 0
        for s in solutions: #przypisanie rozwiązaniom wyniku funkcji fitness
            ranked_solutions.append((fitness(s, index), s))
            index = index + 1
        ranked_solutions.sort()
        print(f"=== Gen {gen + 1} best solution ===")
        print(ranked_solutions[0])
        overall_solutions.append(ranked_solutions[0])
        #TODO warunek stopu
        best_solutions = ranked_solutions[:definitions.GENETIC_ALGORITHM_NUMBER_OF_BEST_INDIVIDUALS] #najlepsze osobniki w danej generacji
        elements = []
        for element in range(definitions.GENETIC_ALGORITHM_COSTS_AMOUNT):
            elems = []
            elements.append(elems)
        for solution in best_solutions:
            for element in range(definitions.GENETIC_ALGORITHM_COSTS_AMOUNT):
                elements[element].append(solution[1][element])
        next_generation = [] #nowa ganeracja
        e = []
        for individual in range(definitions.GENETIC_ALGORITHM_NUMBER_OF_INDIVIDUALS): #liczba osobników w kolejnej generacji
            for el in range(definitions.GENETIC_ALGORITHM_COSTS_AMOUNT):
                #mutacje
                e.append(random.choice(elements[el]) * random.uniform(0.99, 1.01))
            next_generation.append(e)
        solutions = next_generation #zastąpnienie osobników nową generacją
    overall_solutions.sort()
    for _ in range(definitions.GENETIC_ALGORITHM_COSTS_AMOUNT): #przyspianie finalnych kosztów astara
        astar_costs[_] = overall_solutions[0][1][_]
    return astar_costs
def fitness(astar_costs, index):
    ans = harvest(astar_costs, index)
    if ans == 0: #TODO
        return 0
    else:
        return 1 / ans
def harvest(astar_costs, index):
    #kolejność alfabetyczna
    definitions.BEETROOTS_ADULT_COST = astar_costs[0]
    definitions.BEETROOTS_GROW_COST = astar_costs[1]
    definitions.CARROTS_ADULT_COST = astar_costs[2]
    definitions.CARROTS_GROW_COST = astar_costs[3]
    definitions.DIRT_COST = astar_costs[4]
    definitions.FARMLAND_DRY_COST = astar_costs[5]
    definitions.FARMLAND_WET_COST = astar_costs[6]
    definitions.FLOWER_DANDELION_COST = astar_costs[7]
    definitions.POTATOES_ADULT_COST = astar_costs[8]
    definitions.POTATOES_GROW_COST = astar_costs[9]
    definitions.STATION_COST = astar_costs[10]
    definitions.WHEAT_ADULT_COST = astar_costs[11]
    definitions.WHEAT_GROW_COST = astar_costs[12]
    #tworzenie podstawowych obiektów
    map1 = map.Map([])
    map1.create_base_map()
    move_list = ["rotate_left", "move", "move", "move", "move", "move", "move", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "move", "move", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "rotate_left", "move", "rotate_left", "rotate_left", "rotate_left", "move"] #początkowe ruchy
    amount_of_seeds_dict = {"beetroot": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE, "carrot": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE, "potato": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE, "wheat": definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE}
    collected_plants_dict_cart = {"beetroot": 0, "carrot": 0, "potato": 0, "wheat": 0}
    collected_plants_dict_station = {"beetroot": 0, "carrot": 0, "potato": 0, "wheat": 0}
    fertilizer_dict = {"beetroot": definitions.CART_FERTILIZER, "carrot": definitions.CART_FERTILIZER, "potato": definitions.CART_FERTILIZER, "wheat": definitions.CART_FERTILIZER}
    station1 = station.Station(collected_plants_dict_station)
    cart1 = cart.Cart(amount_of_seeds_dict, collected_plants_dict_cart, definitions.CART_DIRECTION_WEST, fertilizer_dict, definitions.CART_FUEL, definitions.CART_WATER_LEVEL, 0 * definitions.BLOCK_SIZE, 0 * definitions.BLOCK_SIZE)
    cart1_rect = pygame.Rect(cart1.get_x(), cart1.get_y(), definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
    tree = treelearn.treelearn() #tworzenie drzewa decyzyjnego
    decision = [0] #początkowa decyzja o braku powrotu do stacji (0)
    grow_flower_dandelion = False
    random_movement = False
    for run in range(definitions.GENETIC_ALGORITHM_NUMBER_OF_CART_MOVES): #liczba ruchów wózka
        if not move_list: #jeżeli są jakieś ruchy do wykonania w move_list
            grow_flower_dandelion = True
            istate = graph.Istate(cart1.get_direction(), cart1.get_x() / definitions.BLOCK_SIZE, cart1.get_y() / definitions.BLOCK_SIZE) #stan początkowy wózka (jego orientacja oraz jego aktualne miejsce)
            if plant.Plant.if_any_mature_plant(map1) is True: #jeżeli istnieje jakaś dojrzała roślina
                random_movement = False
                if decision == [0]: #jeżeli decyzja jest 0 (brak powrotu do stacji) to uprawiaj pole
                    move_list = (astar.graphsearch([], astar.f, [], plant.Plant.get_closest_mature_plant(istate, map1), istate, map1, graph.succ))  #lista z ruchami, które należy po kolei wykonać, astar
                else: #jeżeli decyzja jest 1 (powrót do stacji) to wróć do stacji uzupełnić zapasy
                    move_list = (graph.graphsearch([], [], (0, 0), istate, graph.succ)) #lista z ruchami, które należy po kolei wykonać, graphsearch
            else:
                random_movement = True
        elif move_list: #jeżeli move_list nie jest pusta
            cart1.handle_movement(cart1_rect, move_list.pop(0)) #wykonaj kolejny ruch oraz zdejmij ten ruch z początku listy
        if random_movement is True:
            cart1.handle_movement_random(cart1_rect) #wykonuj losowe ruchy
        if grow_flower_dandelion is True:
            plant.Plant.grow_flower_dandelion(map1) #losuj urośnięcie kwiatka dandeliona
        cart1.do_work(cart1_rect, map1, station1) #wykonaj pracę na danym polu
        decision = treelearn.make_decision(cart1.get_all_amount_of_seeds(), cart1.get_all_collected_plants(), cart1.get_all_fertilizer(), cart1.get_fuel(), tree, cart1.get_water_level()) #podejmij decyzję czy wracać do stacji (0 : NIE, 1 : TAK)
        plant.Plant.grow_plants(map1) #zwiększ poziom dojrzałości roślin
    print("individual no.", index + 1, "score:", station1.get_all_collected_plants())
    return station1.get_all_collected_plants()