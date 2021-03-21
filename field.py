class Field:
    def __init__(self, plant, rect, soil):
        self.plant = plant
        self.rect = rect
        self.soil = soil
    def get_plant(self):
        return self.plant
    def set_plant(self, plant):
        self.plant = plant
    def set_rect(self, rect):
        self.rect = rect
    def get_rect(self):
        return self.rect
    def get_soil(self):
        return self.soil
    def set_soil(self, soil):
        self.soil = soil