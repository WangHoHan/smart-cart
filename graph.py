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
def succ(elem):
    actions_list = []
    actions_list.append(("rotate_left", (elem.get_x(), elem.get_y())))
    actions_list.append(("rotate_right", (elem.get_x(), elem.get_y())))
    if tractor.Tractor.is_move_allowed_succ(elem) == "x + 1":
        actions_list.append(("move", (elem.set_x(elem.get_x() + 1), elem.get_y())))
    elif tractor.Tractor.is_move_allowed_succ(elem) == "y - 1":
        actions_list.append(("move", (elem.get_x(), elem.set_y(elem.get_y() - 1))))
    elif tractor.Tractor.is_move_allowed_succ(elem) == "y + 1":
        actions_list.append(("move", (elem.set_x(elem.get_x()), elem.set_y(elem.get_y() + 1))))
    elif tractor.Tractor.is_move_allowed_succ(elem) == "x - 1":
        actions_list.append(("move", (elem.set_x(elem.get_x() - 1), elem.get_y())))
    return actions_list
def graphsearch(fringe, explored, istate, succ, goaltest):
    node = Node(None, istate.get_direction(), None, istate.get_x(), istate.get_y())
    #fringe.add_to_fringe(node)
    fringe.append(node)
    while True:
        if not fringe:
            return False
        #elem = fringe.get_element_from_fringe_pop()
        elem = fringe.pop(0)
        if goal_test(elem, goaltest) is True:
            return explored
        explored.append(elem)
        for (action, state) in succ(elem):
            if state not in fringe and state not in explored:
                x = Node(action, elem.get_direction(), elem, state[0], state[1])
                print(state[0])
                print(state[1])
                print(x.get_action())
                print(x.get_direction())
                print(x.get_parent())

                fringe.append(x)