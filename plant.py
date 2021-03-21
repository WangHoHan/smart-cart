class Plant:
    def __init__(self, name, organic, required_productivity, required_water_level, state):
        self.name = name
        self.organic = organic
        self.required_productivity = required_productivity
        self.required_water_level = required_water_level
        self.state = state
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_organic(self):
        return self.organic
    def set_organic(self, organic):
        self.organic = organic
    def get_required_productivity(self):
        return self.required_productivity
    def set_required_productivity(self, required_productivity):
        self.required_productivity = required_productivity
    def get_required_water_level(self):
        return self.required_water_level
    def set_required_water_level(self, required_water_level):
        self.required_water_level = required_water_level
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state