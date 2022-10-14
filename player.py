import entities
import equipment


class Player:
    player_entity = entities.BaseEntity()
    player_exist = False
    experience_points = 0
    backpack = []
    floor = 0

    def get_backpack_item(self, item):
        if item < 0 or item >= len(self.backpack):
            return None
        else:
            return self.backpack[item]

    def create_player(self, name="", body=1, soul=1, mind=1, hp_b=5, empty=0, earth=0, water=0, energy=0, life=0):
        if self.player_exist:
            return
        self.player_entity = entities.BaseEntity(name, body, soul, mind, hp_b, empty, earth, water, energy, life)
        self.player_exist = True
        self.backpack.append(equipment.load_equipment(1))
        self.backpack.append(equipment.load_equipment(2))

    def get_player_entity(self):
        return self.player_entity

    def add_item(self, x):
        self.backpack.append(equipment.load_equipment(x))


def get_xp_for_next_level(level):
    return max((((level + 1) ^ 2) + 2))
