import entities

player_entity = entities.BaseEntity()
experience_points = 0


def print_player_info():
    print("--Player info--")
    print("Name: " + str(player_entity.get_name()))

    print("-")

    print("Body: " + str(player_entity.get_base_stat(0)))
    print("Soul: " + str(player_entity.get_base_stat(1)))
    print("Mind: " + str(player_entity.get_base_stat(2)))

    print("-")

    print("Stamina:       " + str(player_entity.get_stamina()))
    print("Determination: " + str(player_entity.get_determination()))
    print("Focus:         " + str(player_entity.get_focus()))

    print("-")

    print("Empty:  " + str(player_entity.get_element_original(0)))
    print("Earth:  " + str(player_entity.get_element_original(1)))
    print("Water:  " + str(player_entity.get_element_original(2)))
    print("Energy: " + str(player_entity.get_element_original(3)))
    print("Life:   " + str(player_entity.get_element_original(4)))

    print("-")

    print("Base health: " + str(player_entity.get_health_base()))
    print("Max health:  " + str(player_entity.get_heath_max()))
    print("Health:      " + str(player_entity.get_health()))

    print("-")


def get_xp_for_next_level(level):
    return max((((level + 1) ^ 2) + 2))
