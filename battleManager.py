import entities
import skillProcessor
import worldData as wD
import gameInterface as gI


def process_skill_0(attacker, defender, skill_slot):
    skill = attacker.get_skill(skill_slot)
    damage_multi = 0
    damage_multi += attacker.get_element_real(skill.get_real_type())
    damage_multi = damage_multi * attacker.get_combat_stat(skill.get_dmg_type())
    damage_multi = damage_multi / defender.get_combat_stat(skill.get_dmg_target() + 3)
    defender.deal_damage(int(skill.get_power * damage_multi))
    skill.activate_cooldown()


def load_enemy(enemy_id):
    if enemy_id == 0:
        return None
    all_enemies = open("Data/Enemies.txt", "r")
    result = None
    for enemy_data in all_enemies:
        if enemy_id == 0:
            result = enemy_data
        enemy_id -= 1
    all_enemies.close()
    if result is None:
        return None

    data = result.split(":")
    enemy = entities.get_entity_from_array(data[0].split("|"))
    skills = data[1].split("|").pop()
    for skill in skills:
        enemy.add_skill(skillProcessor.load_skill(int(skill)))

    return enemy


def battle(main_character):
    enemies = []
    encounter = wD.get_random_floor_enemy_encounter(main_character.floor)
    for x in encounter:
        enemies.append(load_enemy(int(x)))
    turn = 0
    gI.print_simple_line("[" +
                         main_character.player_entity.get_name() +
                         "](" +
                         str(main_character.player_entity.get_health()) +
                         "|" +
                         str(main_character.player_entity.get_health_max) +
                         ")")
    gI.print_simple_line("-")
    for enemy in enemies:
        gI.print_simple_line("[" +
                             enemy.get_name() +
                             "](" +
                             str(enemy.get_health()) +
                             "|" +
                             str(enemy.get_health_max) +
                             ")")
        gI.print_simple_line("-")
    gI.separator()
    choosing = True
    skill_menu_text = main_character.player_entity.get_skill(1).get_name()
    for x in range(2, 9):
        if main_character.player_entity.get_skill(x) is not None:
            skill_menu_text += "," + main_character.player_entity.get_skill(x).get_name()
        else:
            break

    battling = True
    while battling:
        while choosing:
            gI.print_simple_menu(skill_menu_text)
            choiche = int(gI.get_input("Choose a skill to use: "))
            if choiche < 0 or choiche > 8:
                gI.print_simple_line("Not a valid choice")
                gI.separator()
                continue
            if main_character.player_entity.get_skill(choiche) is None:
                gI.print_simple_line("Not a valid choice")
                gI.separator()
                continue
            if not main_character.player_entity.get_skill(choiche).can_use():
                gI.print_simple_line("Still on cooldown")
                gI.separator()
                continue
            choosing = False

        choosing = True
        target = -1
        enemy_names = enemies[0].get_name()
        for enemy in enemies:
            if target == -1:
                x = 0
                continue
            enemy_names += "," + enemy.get_name()

        while choosing:
            target = 0
            gI.print_simple_menu(enemy_names)
            target = gI.get_input("Choose a enemy to attack: ")
            if target < 1 or target > len(enemies):
                gI.print_simple_line("Not a valid target")
                gI.separator()
                continue
            choosing = False

