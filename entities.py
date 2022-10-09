import specialMath as sM


class BaseEntity:

    # base
    def __init__(self, name="", body=1, soul=1, mind=1, hp_b=5, empty=0, earth=0, water=0, energy=0, life=0):
        self.body = body
        self.soul = soul
        self.mind = mind
        self.health_base = hp_b
        self.empty_base = empty
        self.earth_base = earth
        self.water_base = water
        self.energy_base = energy
        self.life_base = life
        self.update_all_stats()
        self.name = name

    def get_body(self):
        return self.body

    def get_mind(self):
        return self.mind

    def get_soul(self):
        return self.soul

    def get_health_base(self):
        return self.health_base

    def get_empty_base(self):
        return self.empty_base

    def get_earth_base(self):
        return self.earth_base

    def get_water_base(self):
        return self.water_base

    def get_energy_base(self):
        return self.energy_base

    def get_life_base(self):
        return self.life_base

    def get_base_stat(self, x):
        if x == 0:
            return self.get_body() + self.get_equipment_boost(x + 5)
        if x == 1:
            return self.get_soul() + self.get_equipment_boost(x + 5)
        if x == 2:
            return self.get_mind() + self.get_equipment_boost(x + 5)
        return 0

    def get_element_original(self, x):
        if x == 0:
            return self.get_empty_base() + self.get_equipment_boost(x)
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

    def get_element_real(self, x):
        if 0 <= x <= 4:
            return sM.real_element_state(self.get_element_original(0), self.get_element_original(x))
        elif 5 <= x <= 9:
            return sM.real_element_state(self.get_element_original(1), self.get_element_original(x-5))
        elif 10 <= x <= 14:
            return sM.real_element_state(self.get_element_original(2), self.get_element_original(x-10))
        elif 15 <= x <= 19:
            return sM.real_element_state(self.get_element_original(3), self.get_element_original(x-15))
        elif 20 <= x <= 24:
            return sM.real_element_state(self.get_element_original(4), self.get_element_original(x-20))

    def get_name(self):
        return self.name

    # derived

    base_sum = 1  # body + soul + mind

    # (heavy + base_sum)/2 * (1 + (level-1/4))
    stamina = 1  # body heavy
    focus = 1  # mind heavy
    determination = 1  # soul heavy

    health_max = 1  # level + base_sum * health_base
    health = 1

    def get_base_sum(self):
        return self.base_sum

    def get_stamina(self):
        return self.stamina

    def get_focus(self):
        return self.focus

    def get_determination(self):
        return self.determination

    def get_heath_max(self):
        return self.health_max

    def get_health(self):
        return self.health

    def update_base_sum(self):
        self.base_sum = self.get_base_stat(0) + self.get_base_stat(1) + self.get_base_stat(2)

    def update_constitutions(self):
        self.stamina = int((self.get_base_stat(0) + self.base_sum) / 2)
        self.focus = int((self.get_base_stat(1) + self.base_sum) / 2)
        self.determination = int((self.get_base_stat(2) + self.base_sum) / 2)

    def update_max_health(self):
        self.health_max = int(self.health_base * self.base_sum)

    def reset_health(self):
        self.health = self.get_heath_max()

    def update_all_stats(self):
        self.update_base_sum()
        self.update_constitutions()
        self.update_max_health()
        self.reset_health()

    # skills

    skill_1 = None
    skill_2 = None
    skill_3 = None
    skill_4 = None
    skill_5 = None
    skill_6 = None
    skill_7 = None
    skill_8 = None

    def get_skill(self, skill):
        if skill < 1 or skill > 8:
            return None
        elif skill == 1:
            return self.skill_1
        elif skill == 2:
            return self.skill_2
        elif skill == 3:
            return self.skill_3
        elif skill == 4:
            return self.skill_4
        elif skill == 5:
            return self.skill_5
        elif skill == 6:
            return self.skill_6
        elif skill == 7:
            return self.skill_7
        elif skill == 8:
            return self.skill_8

    def get_quantity_skills(self):
        for x in range(1, 9):
            if self.get_skill(x) is None:
                return x - 1
        return 8

    def get_first_open_skill_slot(self):
        x = self.get_quantity_skills()
        if x < 8:
            return x + 1
        else:
            return 0

    def has_open_skill_slot(self):
        if 0 <= self.get_quantity_skills() < 8:
            return True
        else:
            return False

    def lower_cooldown(self):
        for x in range(1,9):
            if self.get_skill(x) is not None:
                self.get_skill(x).lower_cooldown()

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
        if self.get_accessory() is not None:
            if self.get_accessory().get_bonus_type_1() == x:
                b += self.get_accessory().get_bonus_amount_1()
            if self.get_accessory().get_bonus_type_2() == x:
                b += self.get_accessory().get_bonus_amount_2()
            if self.get_accessory().get_bonus_type_3() == x:
                b += self.get_accessory().get_bonus_amount_3()

        if self.get_armor() is not None:
            if self.get_armor().get_bonus_type_1() == x:
                b += self.get_armor().get_bonus_amount_1()
            if self.get_armor().get_bonus_type_2() == x:
                b += self.get_armor().get_bonus_amount_2()
            if self.get_armor().get_bonus_type_3() == x:
                b += self.get_armor().get_bonus_amount_3()

        if self.get_weapon() is not None:
            if self.get_weapon().get_bonus_type_1() == x:
                b += self.get_weapon().get_bonus_amount_1()
            if self.get_weapon().get_bonus_type_2() == x:
                b += self.get_weapon().get_bonus_amount_2()
            if self.get_weapon().get_bonus_type_3() == x:
                b += self.get_weapon().get_bonus_amount_3()

        return b
