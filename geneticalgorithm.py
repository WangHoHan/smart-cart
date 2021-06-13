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
    if os.path.exists("resources/genetic_algorithm/optimal.pkl"): #jeżeli drzewo jest zapisane w pliku to odczytaj
        astar_costs = pickle.load(open(os.path.join('resources/genetic_algorithm', "optimal.pkl"), "rb"))
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
        print(definitions.BEETROOTS_ADULT_COST)
        print(definitions.BEETROOTS_GROW_COST)
    else:
        astar_costs = [definitions.BEETROOTS_ADULT_COST, definitions.BEETROOTS_GROW_COST, definitions.CARROTS_ADULT_COST, definitions.CARROTS_GROW_COST, definitions.DIRT_COST, definitions.FARMLAND_DRY_COST, definitions.FARMLAND_WET_COST, definitions.FLOWER_DANDELION_COST, definitions.POTATOES_ADULT_COST, definitions.POTATOES_GROW_COST, definitions.STATION_COST, definitions.WHEAT_ADULT_COST, definitions.WHEAT_GROW_COST]
        astar_costs = make_generations(astar_costs)
        pickle.dump(astar_costs, open(os.path.join('resources/genetic_algorithm', "optimal.pkl"), "wb"))

def fitness(astar_costs):
    ans = solution(astar_costs)
    if ans == 0:
        return 0
    else:
        return 1 / ans
def solution(astar_costs):
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
    for run in range(1000): #liczba ruchów wózka
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



    print("Ile zebrał: ", station1.get_collected_plants("beetroot") + station1.get_collected_plants("carrot") + station1.get_collected_plants("potato") + station1.get_collected_plants("wheat"))
    return station1.get_collected_plants("beetroot") + station1.get_collected_plants("carrot") + station1.get_collected_plants("potato") + station1.get_collected_plants("wheat")



def make_generations(astar_costs):
    solutions = []
    ans = []
    for s in range(10): #liczba osobników zerowej generacji
        solutions.append((random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)))
    for i in range(10): #liczba generacji
        ranked_solutions = []
        for s in solutions:
            ranked_solutions.append((fitness(s), s))
        ranked_solutions.sort()
        print(f"=== Gen {i + 1} best solution ===")
        #print(f"=== Gen {i} best solutions ===")
        print(ranked_solutions[0])
        ans.append(ranked_solutions[0])
        print(ans)

        #można dodać warunek stopu

        best_solutions = ranked_solutions[:4] #najlepsze 4 osobniki w danej generacji
        elements1 = []
        elements2 = []
        elements3 = []
        elements4 = []
        elements5 = []
        elements6 = []
        elements7 = []
        elements8 = []
        elements9 = []
        elements10 = []
        elements11 = []
        elements12 = []
        elements13 = []
        for s in best_solutions:
            elements1.append(s[1][0])
            elements2.append(s[1][1])
            elements3.append(s[1][2])
            elements4.append(s[1][3])
            elements5.append(s[1][4])
            elements6.append(s[1][5])
            elements7.append(s[1][6])
            elements8.append(s[1][7])
            elements9.append(s[1][8])
            elements10.append(s[1][9])
            elements11.append(s[1][10])
            elements12.append(s[1][11])
            elements13.append(s[1][12])

        new_gen = []
        for i in range(10):            # liczba osobników w kolejnej generacji
            e1 = random.choice(elements1) * random.uniform(0.99, 1.01)          # mutacje
            e2 = random.choice(elements2) * random.uniform(0.99, 1.01)
            e3 = random.choice(elements3) * random.uniform(0.99, 1.01)
            e4 = random.choice(elements4) * random.uniform(0.99, 1.01)
            e5 = random.choice(elements5) * random.uniform(0.99, 1.01)
            e6 = random.choice(elements6) * random.uniform(0.99, 1.01)
            e7 = random.choice(elements7) * random.uniform(0.99, 1.01)
            e8 = random.choice(elements8) * random.uniform(0.99, 1.01)
            e9 = random.choice(elements9) * random.uniform(0.99, 1.01)
            e10 = random.choice(elements10) * random.uniform(0.99, 1.01)
            e11 = random.choice(elements11) * random.uniform(0.99, 1.01)
            e12 = random.choice(elements12) * random.uniform(0.99, 1.01)
            e13 = random.choice(elements13) * random.uniform(0.99, 1.01)

            new_gen.append((e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13))

        solutions = new_gen
    ans.sort()
    astar_costs[0] = ans[0][1][0]
    astar_costs[1] = ans[0][1][1]
    astar_costs[2] = ans[0][1][2]
    astar_costs[3] = ans[0][1][3]
    astar_costs[4] = ans[0][1][4]
    astar_costs[5] = ans[0][1][5]
    astar_costs[6] = ans[0][1][6]
    astar_costs[7] = ans[0][1][7]
    astar_costs[8] = ans[0][1][8]
    astar_costs[9] = ans[0][1][9]
    astar_costs[10] = ans[0][1][10]
    astar_costs[11] = ans[0][1][11]
    astar_costs[12] = ans[0][1][12]
    return astar_costs