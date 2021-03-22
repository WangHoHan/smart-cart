class Soil:
    def __init__(self, state, water_level):
        self.state = state
        self.water_level = water_level
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_water_level(self):
        return self.water_level
    def set_water_level(self, water_level):
        self.water_level = water_level