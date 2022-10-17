import entities
import skillProcessor

def load_enemy(enemy_id):
    if enemy_id == 0:
        return None
    all_enemies = open("Data/Enemies.txt", "r")
    result = None
    for skill in all_enemies:
        if enemy_id == 0:
            result = skill
        enemy_id -= 1
    all_enemies.close()
    if result is None:
        return None
    enemy = entities.l
    return loaded

class Battle:
    turn = 0
    player_entity = None
    enemy_entity_1 = None
    enemy_entity_2 = None
    enemy_entity_3 = None
