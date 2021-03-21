class Soil:
    def __init__(self, name, state, water_level):
        self.name = name
        self.state = state
        self.water_level = water_level
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_water_level(self):
        return self.water_level
    def set_required_water_level(self, water_level):
        self.water_level = water_level