class Field:
    def __init__(self, x, y, plant, soil):
        self.x = x
        self.y = y
        self.plant = plant
        self.soil = soil
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
    def get_plant(self):
        return self.plant
    def set_plant(self, plant):
        self.plant = plant
    def get_soil(self):
        return self.soil
    def set_soil(self, soil):
        self.soil = soil