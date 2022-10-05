import specialMath as sM


class BaseSkill:
    def __init__(self, name="", power=0,  dmg_type=0, dmg_target=0, main=0, sub=0):
        self.name = name
        self.power = power

        # 0 = stamina, 1 = focus, 2 = determination
        self.dmg_type = dmg_type
        self.dma_target = dmg_target

        # 0 = typeless, 1 = earth, 2 = water, 3 = energy, 4 = life
        self.main_type = main
        self.sub_type = sub

        self.real_type = (self.main_type * 5) + self.sub_type

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_main_type(self):
        return self.main_type

    def get_sub_type(self):
        return self.sub_type

    def get_real_type(self):
        return self.real_type

    def calculate_damage(self, main, sub, mult):
        if main < 0 or main > 4 or sub < 0 or sub > 4:
            return 0
        dmg = ((main * 3) + sub)/4 * self.power * mult
        return sM.round_down(dmg)


