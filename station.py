class Station:
    def __init__(self, collected_plants):
        self.collected_plants = collected_plants
    def get_collected_plants(self, name):
        return self.collected_plants[name]
    def set_collected_plants(self, name, value):
        self.collected_plants[name] = value