import definitions
class Tractor:
    def __init__(self, x, y):
        self.x = x = 0
        self.y = y = 0
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
    def move_down(self):
        self.y = self.y + definitions.VEL
    def move_left(self):
        self.x = self.x - definitions.VEL
    def move_right(self):
        self.x = self.x + definitions.VEL
    def move_up(self):
        self.y = self.y - definitions.VEL