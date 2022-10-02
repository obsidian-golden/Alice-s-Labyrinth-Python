import specialMath as sM
import math


class BaseEntity:

    # base
    def __init__(self, name="", body=1, soul=1, mind=1, hp_b=5, level=0, earth=1, water=1, energy=1, life=1):
        self.body = body
        self.mind = mind
        self.soul = soul
        self.level = sM.clamp(level, 1, 50)
        self.health_base = hp_b
        self.earth_base = earth
        self.water_base = water
        self.energy_base = energy
        self.life_base = life
        self.update_all_stats()
        self.name = name

    # derived

    base_sum = 1  # body + soul + mind

    # (heavy + base_sum)/2 * (1 + (level-1/4))
    stamina = 1  # body heavy
    focus = 1  # mind heavy
    determination = 1  # soul heavy

    health_max = 1  # level + base_sum * 50/health_reduction
    health = 1

    def update_base_sum(self):
        self.base_sum = self.body + self.soul + self.mind

    def update_constitutions(self):
        self.stamina = (self.body + self.base_sum) / 2 * (1 + (self.level - 1 / 4))
        self.focus = (self.mind + self.base_sum) / 2 * (1 + (self.level - 1 / 4))
        self.determination = (self.soul + self.base_sum) / 2 * (1 + (self.level - 1 / 4))

    def update_max_health(self):
        self.health_max = int((self.level + self.base_sum) * self.health_base)

    def update_all_stats(self):
        self.update_base_sum()
        self.update_constitutions()
        self.update_max_health()

    # skills

    skill_1 = 0
    skill_2 = 0
    skill_3 = 0
    skill_4 = 0
    skill_5 = 0
    skill_6 = 0
    skill_7 = 0
    skill_8 = 0

    def get_skill(self, skill):
        if skill < 1 or skill > 8:
            return 0
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


class Player(BaseEntity):

    experience_points = 0

    def get_level_from_xp(self):
        return sM.clamp(int(math.sqrt(self.experience_points - 2)), 1, 50)

    def get_xp_for_next_level(self):
        return max((((self.level + 1) ^ 2) + 2) - self.experience_points, 0)
