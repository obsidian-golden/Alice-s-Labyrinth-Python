class BaseEquipment:
    def __init__(self, name="", slot=0, b_t_1=0, b_a_1=0, b_t_2=0, b_a_2=0, b_t_3=0, b_a_3=0):
        self.name = name
        # 0 = accessory, 1 = armor, 2 = weapon
        self.slot = slot
        # 0 = "none", 1 = earth, 2 = water, 3 = energy, 4 = life
        self.bonus_type_1 = b_t_1
        self.bonus_amount_1 = b_a_1
        self.bonus_type_2 = b_t_2
        self.bonus_amount_2 = b_a_2
        self.bonus_type_3 = b_t_3
        self.bonus_amount_3 = b_a_3

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
