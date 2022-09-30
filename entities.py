import specialMath as sM


class BaseEntity:

    # base

    level = 1  # max = 50
    experience_points = 1

    body = 1
    soul = 1
    mind = 1

    # derived

    base_sum = 1

    # (heavy + base_sum)/2 * (1 + (level-1/4))
    stamina = 1  # body heavy
    focus = 1  # mind heavy
    determination = 1  # soul heavy

    health_reduction = 3
    health_max = 1  # level + base_sum * 5/health_reduction
    health = 1  #

    def __init__(self, body, soul, mind, xp):
        self.body = body
        self.soul = soul
        self.mind = mind
        self.experience_points = xp

    def calculate_level(self):
        tlevel = sM.round_down((((self.experience_points ^ 2)/4) * self.experience_points) * 1/5)
        self.level = sM.in_range(tlevel, 50, 1)
