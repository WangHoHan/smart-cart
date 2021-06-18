import cart
import copy


class Istate:  # stan początkowy wózka (strona, w którą patrzy, miejsce, w którym się on znajduje)
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


class Node:  # wierzchołek grafu
    def __init__(self, action, direction, parent, x, y):
        self.action = action  # akcja jaką ma wykonać (obróc się w lewo, obróć się w prawo, ruch do przodu)
        self.direction = direction
        self.parent = parent  # ojciec wierzchołka
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


def goal_test(goaltest,
              elem):  # funkcja sprawdzająca czy położenie wózka równa się położeniu punktu docelowego, jeśli tak zwraca prawdę, w przeciwnym wypadku fałsz
    if elem.get_x() == goaltest[0] and elem.get_y() == goaltest[1]:
        return True
    else:
        return False


def graphsearch(explored, fringe, goaltest, istate, succ):  # przeszukiwanie grafu wszerz
    node = Node(None, istate.get_direction(), None, istate.get_x(),
                istate.get_y())  # wierzchołek początkowy, stworzony ze stanu początkowego wózka
    fringe.append(node)  # wierzchołki do odwiedzenia
    while True:
        if not fringe:
            return False
        elem = fringe.pop(0)  # zdejmujemy wierzchołek z kolejki fringe i rozpatrujemy go
        temp = copy.copy(elem)
        if goal_test(goaltest,
                     elem) is True:  # jeżeli osiągniemy cel w trakcie przeszukiwania grafu wszerz (wjedziemy na pole docelowe) : zwracamy listę ruchów, po których wykonaniu dotrzemy na miejsce
            return print_moves(elem)
        explored.append(elem)  # dodajemy wierzchołek do listy wierzchołków odwiedzonych
        for (action, state) in succ(
                temp):  # iterujemy po wszystkich możliwych akcjach i stanach otrzymanych dla danego wierzchołka grafu
            fringe_tuple = []
            explored_tuple = []
            for x in fringe:
                fringe_tuple.append((x.get_direction(), x.get_x(), x.get_y()))
            for x in explored:
                explored_tuple.append((x.get_direction(), x.get_x(), x.get_y()))
            if state not in fringe_tuple and state not in explored_tuple:  # jeżeli stan nie znajduje się na fringe oraz nie znajduje się w liście wierzchołków odwiedzonych
                x = Node(action, state[0], elem, state[1],
                         state[2])  # stworzenie nowego wierzchołka, którego rodzicem jest elem
                fringe.append(x)  # dodanie wierzchołka na fringe


def print_moves(elem):  # zwraca listę ruchów jakie należy wykonać by dotrzeć do punktu docelowego
    moves_list = []
    while (elem.get_parent() != None):
        moves_list.append(elem.get_action())
        elem = elem.get_parent()
    moves_list.reverse()
    return moves_list


def succ(
        elem):  # funkcja następnika, przypisuje jakie akcje są możliwe do wykonania na danym polu oraz jaki będzie stan (kierunek, położenie) po wykonaniu tej akcji
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
    if cart.Cart.is_move_allowed_succ(elem) == "x + 1":
        actions_list.append(("move", (elem.get_direction(), temp_move_east, elem.get_y())))
    elif cart.Cart.is_move_allowed_succ(elem) == "y - 1":
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_north)))
    elif cart.Cart.is_move_allowed_succ(elem) == "y + 1":
        actions_list.append(("move", (elem.get_direction(), elem.get_x(), temp_move_south)))
    elif cart.Cart.is_move_allowed_succ(elem) == "x - 1":
        actions_list.append(("move", (elem.get_direction(), temp_move_west, elem.get_y())))
    return actions_list
