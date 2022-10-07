import entities
import specialMath as sM
import math


class Player(entities.BaseEntity):

    experience_points = 0

    def get_experience_points(self):
        return self.experience_points

    def set_experience_points(self, xp):
        if self.experience_points - xp < 0:
            self.experience_points = 0
        else:
            self.experience_points = int(xp)

    def get_level_from_xp(self):
        return sM.clamp(int(math.sqrt(self.experience_points - 2)), 1, 50)

    def get_xp_for_next_level(self):
        return max((((self.level + 1) ^ 2) + 2) - self.experience_points, 0)

    # equipment

    accessory = None
    armor = None
    weapon = None

    def get_accessory(self):
        return self.accessory

    def get_armor(self):
        return self.armor

    def get_weapon(self):
        return self.weapon

    def get_equipment_boost(self, x):
        b = 0

        if self.get_accessory().get_bonus_type_1() == x:
            b += self.get_accessory().get_bonus_amount_1()
        if self.get_accessory().get_bonus_type_2() == x:
            b += self.get_accessory().get_bonus_amount_2()
        if self.get_accessory().get_bonus_type_3() == x:
            b += self.get_accessory().get_bonus_amount_3()

        if self.get_armor().get_bonus_type_1() == x:
            b += self.get_armor().get_bonus_amount_1()
        if self.get_armor().get_bonus_type_2() == x:
            b += self.get_armor().get_bonus_amount_2()
        if self.get_armor().get_bonus_type_3() == x:
            b += self.get_armor().get_bonus_amount_3()

        if self.get_weapon().get_bonus_type_1() == x:
            b += self.get_weapon().get_bonus_amount_1()
        if self.get_weapon().get_bonus_type_2() == x:
            b += self.get_weapon().get_bonus_amount_2()
        if self.get_weapon().get_bonus_type_3() == x:
            b += self.get_weapon().get_bonus_amount_3()

        return b

    def get_element_original(self, x):
        if x == 0:
            return self.get_none_base() + self.get_equipment_boost(x)
        elif x == 1:
            return self.get_earth_base() + self.get_equipment_boost(x)
        elif x == 2:
            return self.get_water_base() + self.get_equipment_boost(x)
        elif x == 3:
            return self.get_energy_base() + self.get_equipment_boost(x)
        elif x == 4:
            return self.get_life_base() + self.get_equipment_boost(x)
        else:
            return 0