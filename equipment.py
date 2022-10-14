def equipment_from_string(stats="Default|0|0|00|0|00|0|00|0|00|/n"):
    for x in stats:
        print(x)
    cut = stats.split("|")
    return BaseEquipment(cut[0],
                         int(cut[1]),
                         int(cut[2]),
                         int(cut[3]),
                         int(cut[4]),
                         int(cut[5]),
                         int(cut[6]),
                         int(cut[7]),
                         int(cut[8]),
                         int(cut[9])
                         )


def load_equipment(equip_id):
    all_skills = open("Data/Equipment.txt", "r")
    result = None
    for skill in all_skills:
        if equip_id == 0:
            result = skill
        equip_id -= 1
    all_skills.close()
    if result is None:
        return BaseEquipment()
    loaded = equipment_from_string(result)
    return loaded


class BaseEquipment:
    def __init__(self, name="", slot=0, b_t_1=0, b_a_1=0, b_t_2=0, b_a_2=0, b_t_3=0, b_a_3=0, b_t_4=0, b_a_4=0):
        self.name = name
        # 0 = accessory, 1 = armor, 2 = weapon
        self.slot = slot
        # 0 = empty, 1 = earth, 2 = water, 3 = energy, 4 = life
        self.bonus_type_1 = b_t_1
        self.bonus_amount_1 = b_a_1
        self.bonus_type_2 = b_t_2
        self.bonus_amount_2 = b_a_2
        # 0 = p attack, 1 = p defense, 2 = s attack, 3 = s defense, 4 = m attack, 5 = m defense
        self.bonus_type_3 = b_t_3
        self.bonus_amount_3 = b_a_3
        self.bonus_type_4 = b_t_4
        self.bonus_amount_4 = b_a_4

    def get_name(self):
        return self.name

    def get_slot(self):
        return self.slot

    def get_bonus_type_1(self):
        return self.bonus_type_1

    def get_bonus_amount_1(self):
        return self.bonus_amount_1

    def get_bonus_type_2(self):
        return self.bonus_type_2

    def get_bonus_amount_2(self):
        return self.bonus_amount_2

    def get_bonus_type_3(self):
        return self.bonus_type_3

    def get_bonus_amount_3(self):
        return self.bonus_amount_3

    def get_bonus_type_4(self):
        return self.bonus_type_4

    def get_bonus_amount_4(self):
        return self.bonus_amount_4
