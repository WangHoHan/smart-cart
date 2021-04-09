import definitions
class Harvest: #lista dojrzałych roślin
    def __init__(self, harvest):
        self.harvest = harvest
    def get_harvest(self):
        return self.harvest
    def set_harvest(self, harvest):
        self.harvest = harvest
    def add_to_harvest(self, value):
        self.harvest.append(value)
    def remove_element_from_harvest(self, value): #usuwa element z listy o wartości value
        self.harvest.remove(value)
    def find_grown_plants(self, map1): #szuka, na których polach są dojrzałe rośliny
        for i in range(definitions.WIDTH_AMOUNT):
            for j in range(definitions.HEIGHT_AMOUNT):
                field = map1.get_fields()[i][j]
                if (i * definitions.BLOCK_SIZE,
                    j * definitions.BLOCK_SIZE) not in self.harvest and field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() == definitions.BEETROOTS_MAXIMUM_STATE:
                    self.add_to_harvest((i * definitions.BLOCK_SIZE, j * definitions.BLOCK_SIZE))
                elif (i * definitions.BLOCK_SIZE,
                      j * definitions.BLOCK_SIZE) not in self.harvest and field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() == definitions.CARROTS_MAXIMUM_STATE:
                    self.add_to_harvest((i * definitions.BLOCK_SIZE, j * definitions.BLOCK_SIZE))
                elif (i * definitions.BLOCK_SIZE,
                      j * definitions.BLOCK_SIZE) not in self.harvest and field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() == definitions.POTATOES_MAXIMUM_STATE:
                    self.add_to_harvest((i * definitions.BLOCK_SIZE, j * definitions.BLOCK_SIZE))
                elif (i * definitions.BLOCK_SIZE,
                      j * definitions.BLOCK_SIZE) not in self.harvest and field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() == definitions.WHEAT_MAXIMUM_STATE:
                    self.add_to_harvest((i * definitions.BLOCK_SIZE, j * definitions.BLOCK_SIZE))
