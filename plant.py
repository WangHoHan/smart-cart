import definitions
class Plant:
    def __init__(self, name, state):
        self.name = name #nazwa rośliny np. "wheat"
        self.state = state #etap rozwoju rośliny
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    @staticmethod
    def grow_plants(map1): #metoda statyczna, która zwiększa pole state (etap rozwoju rośliny) dla danej rośliny na danym polu o 1
        for i in range(definitions.WIDTH_AMOUNT):
            for j in range(definitions.HEIGHT_AMOUNT):
                field = map1.get_fields()[i][j]
                if field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.BEETROOTS_MAXIMUM_STATE:
                    field.get_plant().set_state(field.get_plant().get_state() + 1)
                elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.CARROTS_MAXIMUM_STATE:
                    field.get_plant().set_state(field.get_plant().get_state() + 1)
                elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.POTATOES_MAXIMUM_STATE:
                    field.get_plant().set_state(field.get_plant().get_state() + 1)
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.WHEAT_MAXIMUM_STATE:
                    field.get_plant().set_state(field.get_plant().get_state() + 1)