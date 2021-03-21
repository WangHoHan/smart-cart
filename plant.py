class Plant:
    def __init__(self, current_state, maximum_state, name, organic, required_water_level):
        self.current_state = current_state
        self.maximum_state = maximum_state
        self.name = name
        self.organic = organic
        self.required_water_level = required_water_level
    def get_current_state(self):
        return self.current_state
    def set_current_state(self, current_state):
        self.current_state = current_state
    def get_maximum_state(self):
        return self.maximum_state
    def set_maximum_state(self, maximum_state):
        self.maximum_state = maximum_state
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_organic(self):
        return self.organic
    def set_organic(self, organic):
        self.organic = organic
    def get_required_water_level(self):
        return self.required_water_level
    def set_required_water_level(self, required_water_level):
        self.required_water_level = required_water_level