def get_input(x="Choose a option: "):
    return input(x)


def separator():
    print("---------")


def print_simple_menu(options="", offset=1):
    counter = 0
    split_options = options.split(",")
    for option in split_options:
        print("[" + str(counter + offset) + "] " + str(option))
        counter += 1


def print_simple_list(options=""):
    split_options = options.split(",")
    for option in split_options:
        print(str(option))


def print_simple_line(x="a"):
    print(x)


def print_player_info(player):
    print("--Player info--")
    print("Name: " + str(player.player_entity.get_name()))

    print("-")

    print("Physical attack:   " + str(player.player_entity.get_combat_stat(0)))
    print("Physical defence:  " + str(player.player_entity.get_combat_stat(1)))
    print("Spiritual attack:  " + str(player.player_entity.get_combat_stat(2)))
    print("Spiritual defence: " + str(player.player_entity.get_combat_stat(3)))
    print("Mental attack:     " + str(player.player_entity.get_combat_stat(4)))
    print("mental defence:    " + str(player.player_entity.get_combat_stat(5)))

    print("-")

    print("Empty:  " + str(player.player_entity.get_element_original(0)))
    print("Earth:  " + str(player.player_entity.get_element_original(1)))
    print("Water:  " + str(player.player_entity.get_element_original(2)))
    print("Energy: " + str(player.player_entity.get_element_original(3)))
    print("Life:   " + str(player.player_entity.get_element_original(4)))

    print("-")

    print("Max health:  " + str(player.player_entity.get_heath_max()))
    print("Health:      " + str(player.player_entity.get_health()))

    print("-")
