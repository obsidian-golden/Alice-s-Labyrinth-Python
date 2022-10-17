def get_skill_from_array(stats=None):
    if stats is None:
        stats = [0, "", 0, 0, 0, 0, 0, 0]
    if len(stats) < 8:
        for x in range(len(stats), 8):
            if x == 1:
                stats.append("")
                continue
            stats.append(0)
    if stats[0] == 0:
        return BaseSkill(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6])

    return None


def load_skill(skill_id):
    if skill_id == 0:
        return None
    all_skills = open("Data/Skills.txt", "r")
    result = None
    for skill in all_skills:
        if skill_id == 0:
            result = skill.split("|")
        skill_id -= 1
    all_skills.close()
    if result is None:
        return None
    loaded = get_skill_from_array(result)
    return loaded


class BaseSkill:
    def __init__(self, skill_type=0, name="", power=0,  dmg_type=0, dmg_target=0, real=0, cool=0):
        self.skill_type = skill_type
        self.name = name
        self.power = power

        # 0 = physical, 1 = spiritual, 2 = mental
        self.dmg_type = dmg_type

        self.dma_target = dmg_target

        # 0 = void, 1 = sand, 2 = mist, 3 = darkness, 4 = rot
        # 5 = metal, 6 = rock, 7 = crystal, 8 = gravity, 9 = magma
        # 10 = ice, 11 = mud, 12 = ocean, 13 = acid, 14 = poison
        # 15 = light, 16 = sound, 17 = electricity, 18 = magic, 19 = fire
        # 20 = flesh, 21 = bug, 22 = plant, 23 = mushroom, 24 = dragon

        self.cooldown = cool
        self.real_type = real
    timer = 0

    def reset_cooldown(self):
        self.timer = 0

    def activate_cooldown(self):
        self.timer = self.cooldown

    def lower_cooldown(self):
        if self.timer > 0:
            self.timer -= 1

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_real_type(self):
        return self.real_type
