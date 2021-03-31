class Soil:
    def __init__(self, is_fertilized, state, water_level):
        self.is_fertilized = is_fertilized
        self.state = state
        self.water_level = water_level
    def get_is_fertilized(self):
        return self.is_fertilized
    def set_is_fertilized(self, is_fertilized):
        self.is_fertilized = is_fertilized
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_water_level(self):
        return self.water_level
    def set_water_level(self, water_level):
        self.water_level = water_level