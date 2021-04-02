import definitions
import random
class Tractor:
    def __init__(self, amount_of_seeds, collected_plants, fertilizer, fuel, water_level, x, y):
        self.amount_of_seeds = amount_of_seeds
        self.collected_plants = collected_plants
        self.fertilizer = fertilizer
        self.fuel = fuel
        self.water_level = water_level
        self.x = x
        self.y = y
    def get_all_amount_of_seeds(self):
        return self.amount_of_seeds["beetroot"] + self.amount_of_seeds["carrot"] + self.amount_of_seeds["potato"] + self.amount_of_seeds["wheat"]
    def get_amount_of_seeds(self, name):
        return self.amount_of_seeds[name]
    def set_amount_of_seeds(self, name, value):
        self.amount_of_seeds[name] = value
    def get_all_collected_plants(self):
        return self.collected_plants["beetroot"] + self.collected_plants["carrot"] + self.collected_plants["potato"] + self.collected_plants["wheat"]
    def get_collected_plants(self, name):
        return self.collected_plants[name]
    def set_collected_plants(self, name, value):
        self.collected_plants[name] = value
    def get_fertilizer(self, name):
        return self.fertilizer[name]
    def set_fertilizer(self, name, value):
        self.fertilizer[name] = value
    def get_fuel(self):
        return self.fuel
    def set_fuel(self, fuel):
        self.fuel = fuel
    def get_water_level(self):
        return self.water_level
    def set_water_level(self, water_level):
        self.water_level = water_level
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
    def move_down(self):
        self.y = self.y + definitions.BLOCK_SIZE
    def move_left(self):
        self.x = self.x - definitions.BLOCK_SIZE
    def move_right(self):
        self.x = self.x + definitions.BLOCK_SIZE
    def move_up(self):
        self.y = self.y - definitions.BLOCK_SIZE
    def do_work(self, map1, station1, tractor1_rect):
        loop = True
        if self.get_all_amount_of_seeds() == 0:
            loop = False
        x = int(tractor1_rect.x / definitions.BLOCK_SIZE)
        y = int(tractor1_rect.y / definitions.BLOCK_SIZE)
        field = map1.get_fields()[x][y]
        if x == 0 and y == 0:
            station1.set_collected_plants("beetroot", station1.get_collected_plants("beetroot") + self.get_collected_plants("beetroot"))
            self.set_collected_plants("beetroot", 0)
            station1.set_collected_plants("carrot", station1.get_collected_plants("carrot") + self.get_collected_plants("carrot"))
            self.set_collected_plants("carrot", 0)
            station1.set_collected_plants("potato", station1.get_collected_plants("potato") + self.get_collected_plants("potato"))
            self.set_collected_plants("potato", 0)
            station1.set_collected_plants("wheat", station1.get_collected_plants("wheat") + self.get_collected_plants("wheat"))
            self.set_collected_plants("wheat", 0)
            self.set_amount_of_seeds("beetroot", definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE)
            self.set_amount_of_seeds("carrot", definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE)
            self.set_amount_of_seeds("potato", definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE)
            self.set_amount_of_seeds("wheat", definitions.TRACTOR_AMOUNT_OF_SEEDS_EACH_TYPE)
            self.set_fertilizer("beetroot", definitions.TRACTOR_FERTILIZER)
            self.set_fertilizer("carrot", definitions.TRACTOR_FERTILIZER)
            self.set_fertilizer("potato", definitions.TRACTOR_FERTILIZER)
            self.set_fertilizer("wheat", definitions.TRACTOR_FERTILIZER)
            self.set_fuel(definitions.TRACTOR_FUEL)
            self.set_water_level(definitions.TRACTOR_WATER_LEVEL)
        elif field.get_soil().get_state() is False:
            field.get_soil().set_state(True)
        elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is False and self.get_water_level() > 0:
            self.set_water_level(self.get_water_level() - 1)
            field.get_soil().set_water_level(True)
        elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is True and field.get_plant().get_state() == 0:
            while loop is True:
                random1 = random.randint(1, 4)
                if random1 == 1 and self.get_amount_of_seeds("beetroot") > 0:
                    self.set_amount_of_seeds("beetroot", self.get_amount_of_seeds("beetroot") - 1)
                    field.get_plant().set_name("beetroot")
                    field.get_plant().set_state(1)
                    loop = False
                elif random1 == 2 and self.get_amount_of_seeds("carrot") > 0:
                    self.set_amount_of_seeds("carrot", self.get_amount_of_seeds("carrot") - 1)
                    field.get_plant().set_name("carrot")
                    field.get_plant().set_state(1)
                    loop = False
                elif random1 == 3 and self.get_amount_of_seeds("potato") > 0:
                    self.set_amount_of_seeds("potato", self.get_amount_of_seeds("potato") - 1)
                    field.get_plant().set_name("potato")
                    field.get_plant().set_state(1)
                    loop = False
                elif random1 == 4 and self.get_amount_of_seeds("wheat") > 0:
                    self.set_amount_of_seeds("wheat", self.get_amount_of_seeds("wheat") - 1)
                    field.get_plant().set_name("wheat")
                    field.get_plant().set_state(1)
                    loop = False
        elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.BEETROOTS_MAXIMUM_STATE - definitions.BEETROOTS_GROW_TIME and self.get_fertilizer("beetroot") > 0 and field.get_soil().get_is_fertilized() is False:
            self.set_fertilizer("beetroot", (self.get_fertilizer("beetroot") - 1))
            field.get_soil().set_is_fertilized(True)
            field.get_plant().set_state(field.get_plant().get_state() + definitions.BEETROOTS_GROW_TIME)
        elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.CARROTS_MAXIMUM_STATE - definitions.CARROTS_GROW_TIME and self.get_fertilizer("carrot") > 0 and field.get_soil().get_is_fertilized() is False:
            self.set_fertilizer("carrot", (self.get_fertilizer("carrot") - 1))
            field.get_soil().set_is_fertilized(True)
            field.get_plant().set_state(field.get_plant().get_state() + definitions.CARROTS_GROW_TIME)
        elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.POTATOES_MAXIMUM_STATE - definitions.POTATOES_GROW_TIME and self.get_fertilizer("potato") > 0 and field.get_soil().get_is_fertilized() is False:
            self.set_fertilizer("potato", (self.get_fertilizer("potato") - 1))
            field.get_soil().set_is_fertilized(True)
            field.get_plant().set_state(field.get_plant().get_state() + definitions.POTATOES_GROW_TIME)
        elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() < definitions.WHEAT_MAXIMUM_STATE - definitions.WHEAT_GROW_TIME and self.get_fertilizer("wheat") > 0 and field.get_soil().get_is_fertilized() is False:
            self.set_fertilizer("wheat", (self.get_fertilizer("wheat") - 1))
            field.get_soil().set_is_fertilized(True)
            field.get_plant().set_state(field.get_plant().get_state() + definitions.WHEAT_GROW_TIME)
        elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() == definitions.BEETROOTS_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("beetroot", self.get_collected_plants("beetroot") + 1)
        elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() == definitions.CARROTS_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("carrot", self.get_collected_plants("carrot") + 1)
        elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() == definitions.POTATOES_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("potato", self.get_collected_plants("potato") + 1)
        elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() == definitions.WHEAT_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.TRACTOR_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("wheat", self.get_collected_plants("wheat") + 1)
    def is_move_allowed(self, move, tractor1_rect):
        if move == 1 and tractor1_rect.y + definitions.BLOCK_SIZE + definitions.BLOCK_SIZE <= definitions.HEIGHT:
            return True
        elif move == 2 and tractor1_rect.x - definitions.BLOCK_SIZE >= 0:
            return True
        elif move == 3 and tractor1_rect.x + definitions.BLOCK_SIZE + definitions.BLOCK_SIZE <= definitions.WIDTH:
            return True
        elif move == 4 and tractor1_rect.y - definitions.BLOCK_SIZE >= 0:
            return True
        else:
            return False
    def tractor1_handle_movement(self, tractor1_rect):
        loop = True
        while loop and self.get_fuel() > 0:
            random1 = random.randint(1, 4)
            if random1 == 1 and self.is_move_allowed(1, tractor1_rect) is True:
                self.move_down()
                tractor1_rect.x = self.get_x()
                tractor1_rect.y = self.get_y()
                loop = False
            elif random1 == 2 and self.is_move_allowed(2, tractor1_rect) is True:
                self.move_left()
                tractor1_rect.x = self.get_x()
                tractor1_rect.y = self.get_y()
                loop = False
            elif random1 == 3 and self.is_move_allowed(3, tractor1_rect) is True:
                self.move_right()
                tractor1_rect.x = self.get_x()
                tractor1_rect.y = self.get_y()
                loop = False
            elif random1 == 4 and self.is_move_allowed(4, tractor1_rect) is True:
                self.move_up()
                tractor1_rect.x = self.get_x()
                tractor1_rect.y = self.get_y()
                loop = False
        self.set_fuel(self.get_fuel() - 1)
        if tractor1_rect.x == 0 and tractor1_rect.y == 0:
            self.set_fuel(definitions.TRACTOR_FUEL)
            self.set_water_level(definitions.TRACTOR_WATER_LEVEL)