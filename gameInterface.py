def get_input(x="Choose a option: "):
    return input(x)


def separator():
    print("---------")


def get_element_original_string_from_id(x=0):
    if x < 0 or x > 4:
        x = 0
    elem = ["Empty", "Earth", "Water", "Energy", "Life"]
    return elem[x]


def get_combat_stat_string_from_id(x=0):
    if x < 0 or x > 5:
        x = 0
    stat = ["Physical attack", "Physical defence", "Spiritual attack", "Spiritual defence", "Mental attack", "Mental defense"]
    return stat[x]


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


def get_equipment_slot_string_from_id(x=0):
    if x < 0 or x > 2:
        x = 0
    slot = ["Accessory", "Armor", "Weapon"]
    return slot[x]


def print_equipment_info(equipment):
    if equipment is None:
        print("Not a valid item")
    print(get_equipment_slot_string_from_id(equipment.get_slot()) + ": " + equipment.get_name())
    if equipment.get_bonus_amount_1() != 0:
        print(get_element_original_string_from_id(equipment.get_bonus_type_1()) +
              ": " +
              str(equipment.get_bonus_amount_1()))
        if equipment.get_bonus_amount_2() != 0:
            print(get_element_original_string_from_id(equipment.get_bonus_type_2()) +
                  ": " +
                  str(equipment.get_bonus_amount_2()))
    if equipment.get_bonus_amount_3() != 0:
        print(get_combat_stat_string_from_id(equipment.get_bonus_type_3()) +
              ": " +
              str(equipment.get_bonus_amount_3()))
        if equipment.get_bonus_amount_4() != 0:
            print(get_combat_stat_string_from_id(equipment.get_bonus_type_4()) +
                  ": " +
                  str(equipment.get_bonus_amount_4()))


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

    print("Max health:  " + str(player.player_entity.get_health_max()))
    print("Health:      " + str(player.player_entity.get_health()))

    separator()
