import definitions
import random
class Cart:
    def __init__(self, amount_of_seeds, collected_plants, direction, fertilizer, fuel, water_level, x, y):
        self.amount_of_seeds = amount_of_seeds #amount_of_seeds to słownik, przechowuje informacje o posiadanej ilości ziaren dla danej rośliny
        self.collected_plants = collected_plants #collected_plants to słownik, przechowuje informacje o zebranych plonach
        self.direction = direction #w którą stronę patrzy, zgodnie ze wskazówkami zegara (1 -: godzina 12, 2 : godzina 3, 3 : godzina 6, 4 : godzina 9)
        self.fertilizer = fertilizer #fertilizer to słownik, przechowuje informacje o ilości posiadanego nawozu dla konkretnej rośliny
        self.fuel = fuel #aktualna ilość paliwa
        self.water_level = water_level #aktualna ilość wody do podlewania
        self.x = x
        self.y = y
    def get_all_amount_of_seeds(self): #zwraca łączną ilość ziaren (suma ziaren dla wszystkich roślin)
        return self.amount_of_seeds["beetroot"] + self.amount_of_seeds["carrot"] + self.amount_of_seeds["potato"] + self.amount_of_seeds["wheat"]
    def get_amount_of_seeds(self, name): #zwraca łączną ilość ziaren dla podanej rośliny (name)
        return self.amount_of_seeds[name]
    def set_amount_of_seeds(self, name, value): #dla podanej rośliny (name) ustawia łączną ilość ziaren (value)
        self.amount_of_seeds[name] = value
    def get_all_collected_plants(self): #zwraca łączną ilość zebranych plonów (suma plonów wszystkich roślin)
        return self.collected_plants["beetroot"] + self.collected_plants["carrot"] + self.collected_plants["potato"] + self.collected_plants["wheat"]
    def get_collected_plants(self, name): #zwraca łączną ilość zebranych plonów dla podanej rośliny (name)
        return self.collected_plants[name]
    def set_collected_plants(self, name, value): #dla podanej rośliny (name) ustawia łączną ilość zebranych plonów (value)
        self.collected_plants[name] = value
    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction
    def get_all_fertilizer(self): #zwraca łączną ilość posiadanego nawozu (suma nawozu dla wszystkich roślin)
        return self.fertilizer["beetroot"] + self.fertilizer["carrot"] + self.fertilizer["potato"] + self.fertilizer["wheat"]
    def get_fertilizer(self, name): #zwraca łączną ilość posiadanego nawozu dla podanej rośliny (name)
        return self.fertilizer[name]
    def set_fertilizer(self, name, value): #dla podanej rośliny (name) ustawia ilość posiadanego nawozu (value)
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
    def do_work(self, cart_rect, map1, station1): #jaką pracę wózek ma wykonać na danym polu, na którym aktualnie przebywa (zmienia stan logiczny danego pola)
        loop = True
        if self.get_all_amount_of_seeds() == 0:
            loop = False
        x = int(cart_rect.x / definitions.BLOCK_SIZE)
        y = int(cart_rect.y / definitions.BLOCK_SIZE)
        field = map1.get_fields()[x][y]
        if x == 0 and y == 0:
            self.station_restore(station1)
        elif field.get_plant().get_name() == "flower_dandelion":
            field.get_plant().set_name("none")
            field.get_plant().set_state(0)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
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
        elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() == definitions.BEETROOTS_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.CART_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_name("none")
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("beetroot", self.get_collected_plants("beetroot") + 1)
        elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() == definitions.CARROTS_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.CART_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_name("none")
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("carrot", self.get_collected_plants("carrot") + 1)
        elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() == definitions.POTATOES_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.CART_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_name("none")
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("potato", self.get_collected_plants("potato") + 1)
        elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() == definitions.WHEAT_MAXIMUM_STATE and self.get_all_collected_plants() < definitions.CART_MAXIMUM_COLLECTED_PLANTS:
            field.get_plant().set_name("none")
            field.get_plant().set_state(0)
            field.get_soil().set_is_fertilized(False)
            field.get_soil().set_water_level(False)
            field.get_soil().set_state(False)
            self.set_collected_plants("wheat", self.get_collected_plants("wheat") + 1)
    def handle_movement(self, cart_rect, move): #odpowiada za poruszanie się wózka po mapie
        if self.get_fuel() > 0:
            if move == "move":
                self.move()
            elif move == "rotate_left":
                self.rotate_left()
            elif move == "rotate_right":
                self.rotate_right()
            self.set_fuel(self.get_fuel() - 1)
            cart_rect.x = self.get_x()
            cart_rect.y = self.get_y()
    def handle_movement_random(self, cart_rect): #odpowiada za losowe poruszanie się wózka po mapie
        loop = True
        while loop and self.get_fuel() > 0:
            random1 = random.randint(1, 3)
            if random1 == 1 and self.is_move_allowed(cart_rect) is True:
                self.move()
                cart_rect.x = self.get_x()
                cart_rect.y = self.get_y()
                loop = False
            elif random1 == 2:
                self.rotate_left()
                loop = False
            elif random1 == 3:
                self.rotate_right()
                loop = False
        self.set_fuel(self.get_fuel() - 1)
    def is_move_allowed(self, cart_rect): #sprawdza czy dany ruch, który chce wykonać wózek jest możliwy, zwraca prawdę lub fałsz
        if self.direction == definitions.CART_DIRECTION_EAST and cart_rect.x + definitions.BLOCK_SIZE < definitions.WIDTH_MAP:
            return True
        elif self.direction == definitions.CART_DIRECTION_NORTH and cart_rect.y - definitions.BLOCK_SIZE >= 0:
            return True
        elif self.direction == definitions.CART_DIRECTION_SOUTH and cart_rect.y + definitions.BLOCK_SIZE < definitions.HEIGHT_MAP:
            return True
        elif self.direction == definitions.CART_DIRECTION_WEST and cart_rect.x - definitions.BLOCK_SIZE >= 0:
            return True
        else:
            return False
    @staticmethod
    def is_move_allowed_succ(node): #sprawdza czy dany ruch, który chce wykonać wózek jest możliwy, zwraca pozycje po wykonaniu ruchu, wersja node
        if node.get_direction() == definitions.CART_DIRECTION_EAST and node.get_x() * definitions.BLOCK_SIZE + definitions.BLOCK_SIZE < definitions.WIDTH_MAP:
            return "x + 1"
        elif node.get_direction() == definitions.CART_DIRECTION_NORTH and node.get_y() * definitions.BLOCK_SIZE - definitions.BLOCK_SIZE >= 0:
            return "y - 1"
        elif node.get_direction() == definitions.CART_DIRECTION_SOUTH and node.get_y() * definitions.BLOCK_SIZE + definitions.BLOCK_SIZE < definitions.HEIGHT_MAP:
            return "y + 1"
        elif node.get_direction() == definitions.CART_DIRECTION_WEST and node.get_x() * definitions.BLOCK_SIZE - definitions.BLOCK_SIZE >= 0:
            return "x - 1"
        else:
            return False
    def move(self):
        if self.direction == definitions.CART_DIRECTION_EAST:
            self.x = self.x + definitions.BLOCK_SIZE
        elif self.direction == definitions.CART_DIRECTION_NORTH:
            self.y = self.y - definitions.BLOCK_SIZE
        elif self.direction == definitions.CART_DIRECTION_SOUTH:
            self.y = self.y + definitions.BLOCK_SIZE
        elif self.direction == definitions.CART_DIRECTION_WEST:
            self.x = self.x - definitions.BLOCK_SIZE
    def rotate_left(self):
        if self.direction == 1:
            self.direction = 4
        else:
            self.direction = self.direction - 1
    def rotate_right(self):
        if self.direction == 4:
            self.direction = 1
        else:
            self.direction = self.direction + 1
    def station_restore(self, station1): #aktualizuje stan stacji pod względem oddanych plonów oraz uzupełnia zapasy wózka
        station1.set_collected_plants("beetroot", station1.get_collected_plants("beetroot") + self.get_collected_plants("beetroot"))
        self.set_collected_plants("beetroot", 0)
        station1.set_collected_plants("carrot", station1.get_collected_plants("carrot") + self.get_collected_plants("carrot"))
        self.set_collected_plants("carrot", 0)
        station1.set_collected_plants("potato", station1.get_collected_plants("potato") + self.get_collected_plants("potato"))
        self.set_collected_plants("potato", 0)
        station1.set_collected_plants("wheat", station1.get_collected_plants("wheat") + self.get_collected_plants("wheat"))
        self.set_collected_plants("wheat", 0)
        self.set_amount_of_seeds("beetroot", definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE)
        self.set_amount_of_seeds("carrot", definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE)
        self.set_amount_of_seeds("potato", definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE)
        self.set_amount_of_seeds("wheat", definitions.CART_AMOUNT_OF_SEEDS_EACH_TYPE)
        self.set_fertilizer("beetroot", definitions.CART_FERTILIZER)
        self.set_fertilizer("carrot", definitions.CART_FERTILIZER)
        self.set_fertilizer("potato", definitions.CART_FERTILIZER)
        self.set_fertilizer("wheat", definitions.CART_FERTILIZER)
        self.set_fuel(definitions.CART_FUEL)
        self.set_water_level(definitions.CART_WATER_LEVEL)