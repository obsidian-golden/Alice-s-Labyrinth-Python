import entities
import equipment
import skillProcessor


class Player:
    player_entity = entities.BaseEntity()
    player_exist = False
    experience_points = 0
    backpack = []
    floor = 1

    def get_backpack_item(self, item):
        if item < 0 or item > len(self.backpack):
            return None
        else:
            return self.backpack[item]

    def unequip_item(self, slot):
        if self.get_player_entity().get_equipment(slot) is None:
            return
        self.backpack.append(self.get_player_entity().get_equipment(slot))
        self.get_player_entity().remove_equipment(slot)

    def equip_item(self, item):
        if item < 0 or item >= len(self.backpack):
            return
        item_to_equip = self.backpack[item]
        self.unequip_item(item_to_equip.get_slot())
        self.get_player_entity().set_equipment(item_to_equip)
        self.backpack.pop(item)

    def create_player(self, player):
        if self.player_exist:
            return
        if player is None:
            player = ["", 1, 1, 1, 20, 3, 0, 0, 0, 0]
        self.player_entity = entities.get_entity_from_array(player)
        self.player_exist = True
        self.backpack.append(equipment.load_equipment(1))
        self.backpack.append(equipment.load_equipment(2))
        self.backpack.append(equipment.load_equipment(3))
        self.player_entity.add_skill(skillProcessor.load_skill(2))
        self.player_entity.add_skill(skillProcessor.load_skill(3))
        self.player_entity.add_skill(skillProcessor.load_skill(4))

    def get_player_entity(self):
        return self.player_entity

    def add_item(self, x):
        self.backpack.append(equipment.load_equipment(x))


def get_xp_for_next_level(level):
    return max((((level + 1) ^ 2) + 2))
