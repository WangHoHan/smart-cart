import definitions
class Tractor:
    def __init__(self, amount_of_seeds, collected_plants, fertilizer, fuel, water_level, x, y):
        self.amount_of_seeds = amount_of_seeds
        self.collected_plants = collected_plants
        self.fertilizer = fertilizer
        self.fuel = fuel
        self.water_level = water_level
        self.x = x
        self.y = y
    def get_all_amount_of_seeds(self):
        return self.amount_of_seeds["beetroot"] + self.amount_of_seeds["carrot"] + self.amount_of_seeds["potato"] + self.amount_of_seeds["wheat"]
    def get_amount_of_seeds(self, name):
        return self.amount_of_seeds[name]
    def set_amount_of_seeds(self, name, value):
        self.amount_of_seeds[name] = value
    def get_all_collected_plants(self):
        return self.collected_plants["beetroot"] + self.collected_plants["carrot"] + self.collected_plants["potato"] + self.collected_plants["wheat"]
    def get_collected_plants(self, name):
        return self.collected_plants[name]
    def set_collected_plants(self, name, value):
        self.collected_plants[name] = value
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