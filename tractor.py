import definitions
class Tractor:
    def __init__(self, fertilizer, x, y):
        self.fertilizer = fertilizer
        self.x = x
        self.y = y
    def get_fertilizer(self):
        return self.fertilizer
    def set_fertilizer(self, fertilizer):
        self.fertilizer = fertilizer
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
    def move_down(self):
        self.y = self.y + definitions.BLOCK_SIZE
    def move_left(self):
        self.x = self.x - definitions.BLOCK_SIZE
    def move_right(self):
        self.x = self.x + definitions.BLOCK_SIZE
    def move_up(self):
        self.y = self.y - definitions.BLOCK_SIZE