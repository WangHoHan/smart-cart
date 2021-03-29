import definitions
class Tractor:
    def __init__(self, fertilizer, fuel, water_level, x, y):
        self.fertilizer = fertilizer
        self.fuel = fuel
        self.water_level = water_level
        self.x = x
        self.y = y
    def get_fertilizer(self, name):
        return self.fertilizer[name]
    def set_fertilizer(self, name, value):
        self.fertilizer[name] = value
    def get_fuel(self):
        return self.fuel
    def set_fuel(self, fuel):
        self.fuel = fuel
    def get_water_level(self):
        return self.water_level
    def set_water_level(self, water_level):
        self.water_level = water_level
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