import entities


class Player:
    player_entity = entities.BaseEntity()
    player_exist = False
    experience_points = 0

    def create_player(self, name="", body=1, soul=1, mind=1, hp_b=5, empty=0, earth=0, water=0, energy=0, life=0):
        if self.player_exist:
            return
        self.player_entity = entities.BaseEntity(name, body, soul, mind, hp_b, empty, earth, water, energy, life)
        self.player_exist = True

    def get_player_entity(self):
        return self.player_entity


def get_xp_for_next_level(level):
    return max((((level + 1) ^ 2) + 2))
