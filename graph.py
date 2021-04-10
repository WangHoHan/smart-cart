import copy
import tractor
class Node:
    def __init__(self, action, direction, parent, x, y):
        self.action = action
        self.direction = direction
        self.parent = parent
        self.x = x
        self.y = y
    def get_action(self):
        return self.action
    def set_action(self, action):
        self.action = action
    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction
    def get_parent(self):
        return self.parent
    def set_parent(self, parent):
        self.parent = parent
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
class Istate: #stan początkowy traktora
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y
    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
# class Fringe: #kolejka zawierająca akcje oraz pola do odwiedzenia
#     def __init__(self, fringe):
#         self.fringe = fringe
#     def get_fringe(self):
#         return self.fringe
#     def set_fringe(self, fringe):
#         self.fringe = fringe
#     def add_to_fringe(self, value):
#         self.fringe.append(value)
#     def get_element_from_fringe_pop(self):
#         return self.fringe.pop(0)
def goal_test(elem, goaltest):
    if elem.get_x() == goaltest.get_x() and elem.get_y() == goaltest.get_y(): #goaltest bez getterów
        return True
    else:
        return False
def print_moves(elem, explored):
    moves_list = []
    while (elem.get_parent() != None):
        moves_list.append(elem.get_action())
        elem = elem.get_parent()
    moves_list.reverse()
    return moves_list
def succ(elem):
    actions_list = []
    temp = copy.copy(elem.get_direction())
    if temp == 1:
        temp = 4
    else:
        temp = temp - 1
    actions_list.append(("rotate_left", (temp, elem.get_x(), elem.get_y())))
    temp = copy.copy(elem.get_direction())
    if temp == 4:
        temp = 1
    else:
        temp = temp + 1
    actions_list.append(("rotate_right", (temp, elem.get_x(), elem.get_y())))
    temp_move_south = elem.get_y() + 1
    temp_move_west = elem.get_x() - 1
    temp_move_east = elem.get_x() + 1
    temp_move_north = elem.get_y() - 1
    if tractor.Tractor.is_move_allowed_succ(elem) == "x + 1":
        actions_list.append(("move", (elem.get_direction(), temp_move_east, elem.get_y())))
    elif tractor.Tractor.is_move_allowed_succ(elem) == "y - 1":
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_north)))
    elif tractor.Tractor.is_move_allowed_succ(elem) == "y + 1":
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_south)))
    elif tractor.Tractor.is_move_allowed_succ(elem) == "x - 1":
        actions_list.append(("move", (elem.get_direction(), temp_move_west, elem.get_y())))
    return actions_list
def graphsearch(fringe, explored, istate, succ, goaltest):
    node = Node(None, istate.get_direction(), None, istate.get_x(), istate.get_y()) #może None coś nie gra
    #fringe.add_to_fringe(node)
    fringe.append(node)
    while True:
        if not fringe:
            return False
        #elem = fringe.get_element_from_fringe_pop()
        elem = fringe.pop(0)
        temp = copy.copy(elem) #żeby explored w for succ() nie zmieniało
        if goal_test(elem, goaltest) is True:
            # for x in fringe:
            #     print("action: " + str(x.get_action()))
            #     print("direction: " + str(x.get_direction()))
            #     print("parent: " + str(x.get_parent()))
            #     print("node: " + str(x))
            #     print("x: " + str(x.get_x()))
            #     print("y: " + str(x.get_y()))
            # for x in explored:
            #     print("action ex: " + str(x.get_action()))
            #     print("direction ex: " + str(x.get_direction()))
            #     print("parent ex: " + str(x.get_parent()))
            #     print("node ex: " + str(x))
            #     print("x ex: " + str(x.get_x()))
            #     print("y ex: " + str(x.get_y()))
            return print_moves(elem, explored)
        explored.append(elem)
        for (action, state) in succ(temp):
            fringe_tuple = []
            explored_tuple = []
            for x in fringe:
                fringe_tuple.append((x.get_direction(), x.get_x(), x.get_y()))
            for x in explored:
                explored_tuple.append((x.get_direction(), x.get_x(), x.get_y()))
            if state not in fringe_tuple and state not in explored_tuple:
                x = Node(action, state[0], elem, state[1], state[2])
                # print(x.get_action())
                # print(state[0])
                # print(state[1])
                # print(state[2])
                # print(x.get_direction())
                # print(x.get_parent())
                fringe.append(x)