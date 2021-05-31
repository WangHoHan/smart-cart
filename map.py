import definitions
import field
import plant
import pygame
import soil
class Map:
    def __init__(self, fields):
        self.fields = fields #przechowuje wszystkie pola (Field)
    def get_fields(self):
        return self.fields
    def set_fields(self, fields):
        self.fields = fields
    def create_base_map(self): #wypełnia mapę polami z bazowymi logicznymi wartościami
        for i in range(definitions.WIDTH_AMOUNT):
            temp_map_field = []
            for j in range(definitions.HEIGHT_AMOUNT):
                temp_rect = pygame.Rect(i * definitions.BLOCK_SIZE, j * definitions.BLOCK_SIZE, definitions.BLOCK_SIZE, definitions.BLOCK_SIZE)
                if i == 0 and j == 0:
                    temp_plant = plant.Plant("station", -1)
                else:
                    temp_plant = plant.Plant("none", 0)
                temp_soil = soil.Soil(False, False, False)
                temp_field = field.Field(temp_plant, temp_rect, temp_soil)
                temp_map_field.append(temp_field)
            self.fields.append(temp_map_field)
    def draw_window(self, cart, cart_rect): #rysuje mapę
        self.fill_map()
        if cart.get_direction() == definitions.CART_DIRECTION_EAST:
            definitions.WINDOW.blit(definitions.CART_DIRECTION_EAST_TEXTURE, (cart_rect.x, cart_rect.y))
        elif cart.get_direction() == definitions.CART_DIRECTION_NORTH:
            definitions.WINDOW.blit(definitions.CART_DIRECTION_NORTH_TEXTURE, (cart_rect.x, cart_rect.y))
        elif cart.get_direction() == definitions.CART_DIRECTION_SOUTH:
            definitions.WINDOW.blit(definitions.CART_DIRECTION_SOUTH_TEXTURE, (cart_rect.x, cart_rect.y))
        elif cart.get_direction() == definitions.CART_DIRECTION_WEST:
            definitions.WINDOW.blit(definitions.CART_DIRECTION_WEST_TEXTURE, (cart_rect.x, cart_rect.y))
        pygame.display.update()
    def fill_map(self): #wypełnia mapę teksturami na podstawie logicznego stanu pól
        for i in range(definitions.WIDTH_AMOUNT):
            for j in range(definitions.HEIGHT_AMOUNT):
                field = self.fields[i][j]
                rect = field.get_rect()
                if field.get_plant().get_name() == "station" and field.get_plant().get_state() == -1:
                    block = definitions.STATION
                elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.BEETROOTS_GROW_TIME:
                    block = definitions.BEETROOTS_STAGE_0
                elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 1 * definitions.BEETROOTS_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.BEETROOTS_GROW_TIME:
                    block = definitions.BEETROOTS_STAGE_1
                elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 2 * definitions.BEETROOTS_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.BEETROOTS_GROW_TIME:
                    block = definitions.BEETROOTS_STAGE_2
                elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() == definitions.BEETROOTS_MAXIMUM_STATE:
                    block = definitions.BEETROOTS_STAGE_3
                elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.CARROTS_GROW_TIME:
                    block = definitions.CARROTS_STAGE_0
                elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 1 * definitions.CARROTS_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.CARROTS_GROW_TIME:
                    block = definitions.CARROTS_STAGE_1
                elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 2 * definitions.CARROTS_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.CARROTS_GROW_TIME:
                    block = definitions.CARROTS_STAGE_2
                elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() == definitions.CARROTS_MAXIMUM_STATE:
                    block = definitions.CARROTS_STAGE_3
                elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.POTATOES_GROW_TIME:
                    block = definitions.POTATOES_STAGE_0
                elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 1 * definitions.POTATOES_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.POTATOES_GROW_TIME:
                    block = definitions.POTATOES_STAGE_1
                elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 2 * definitions.POTATOES_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.POTATOES_GROW_TIME:
                    block = definitions.POTATOES_STAGE_2
                elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() == definitions.POTATOES_MAXIMUM_STATE:
                    block = definitions.POTATOES_STAGE_3
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 1 * definitions.WHEAT_GROW_TIME:
                    block = definitions.WHEAT_STAGE_0
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 1 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 2 * definitions.WHEAT_GROW_TIME:
                    block = definitions.WHEAT_STAGE_1
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 2 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 3 * definitions.WHEAT_GROW_TIME:
                    block = definitions.WHEAT_STAGE_2
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 3 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 4 * definitions.WHEAT_GROW_TIME:
                    block = definitions.WHEAT_STAGE_3
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 4 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 5 * definitions.WHEAT_GROW_TIME:
                    block = definitions.WHEAT_STAGE_4
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 5 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 6 * definitions.WHEAT_GROW_TIME:
                    block = definitions.WHEAT_STAGE_5
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 6 * definitions.WHEAT_GROW_TIME and field.get_plant().get_state() <= 7 * definitions.WHEAT_GROW_TIME:
                    block = definitions.WHEAT_STAGE_6
                elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() == definitions.WHEAT_MAXIMUM_STATE:
                    block = definitions.WHEAT_STAGE_7
                elif field.get_soil().get_state() is False:
                    block = definitions.DIRT
                elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is False:
                    block = definitions.FARMLAND_DRY
                elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is True:
                    block = definitions.FARMLAND_WET
                if block == definitions.STATION:
                    definitions.WINDOW.blit(definitions.SPONGE, (rect.x, rect.y))
                elif block != definitions.DIRT or block != definitions.FARMLAND_DRY or block != definitions.FARMLAND_WET:
                    definitions.WINDOW.blit(definitions.FARMLAND_WET, (rect.x, rect.y))
                definitions.WINDOW.blit(block, (rect.x, rect.y))
    def get_field_cost(self, x, y): #zwraca koszt  danego pola
        field = self.fields[x][y]
        if field.get_plant().get_name() == "station" and field.get_plant().get_state() == -1:
            return definitions.STATION_COST
        elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 3 * definitions.BEETROOTS_GROW_TIME:
            return definitions.BEETROOTS_GROW_COST
        elif field.get_plant().get_name() == "beetroot" and field.get_plant().get_state() == definitions.BEETROOTS_MAXIMUM_STATE:
            return definitions.BEETROOTS_ADULT_COST
        elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 3 * definitions.CARROTS_GROW_TIME:
            return definitions.CARROTS_GROW_COST
        elif field.get_plant().get_name() == "carrot" and field.get_plant().get_state() == definitions.CARROTS_MAXIMUM_STATE:
            return definitions.CARROTS_ADULT_COST
        elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 3 * definitions.POTATOES_GROW_TIME:
            return definitions.POTATOES_GROW_COST
        elif field.get_plant().get_name() == "potato" and field.get_plant().get_state() == definitions.POTATOES_MAXIMUM_STATE:
            return definitions.POTATOES_ADULT_COST
        elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() > 0 and field.get_plant().get_state() <= 7 * definitions.WHEAT_GROW_TIME:
            return definitions.WHEAT_GROW_COST
        elif field.get_plant().get_name() == "wheat" and field.get_plant().get_state() == definitions.WHEAT_MAXIMUM_STATE:
            return definitions.WHEAT_ADULT_COST
        elif field.get_soil().get_state() is False:
            return definitions.DIRT_COST
        elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is False:
            return definitions.FARMLAND_DRY_COST
        elif field.get_soil().get_state() is True and field.get_soil().get_water_level() is True:
            return definitions.FARMLAND_WET_COST