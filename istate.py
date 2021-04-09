class Istate: #stan początkowy traktora
    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y
    def get_direction(self):
        return self.direction
    def set_x(self, direction):
        self.direction = direction
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y