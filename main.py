import gameInterface as gI
import characterCreation
import player
import worldData as wD

gI.separator()
gI.print_simple_menu("Start game,Exit")
action = int(gI.get_input())

main_character = player.Player()


def print_player_stats():
    gI.print_player_info(main_character)
    return 1


def manage_inventory():
    gI.print_simple_menu("Show player equipment,Show backpack,Equip item,Show backpack item info,Back")
    x = gI.get_input()
    gI.separator()

    if x == 1:
        gI.print_simple_line("Player equipment: ")
        if main_character.get_player_entity().get_weapon() is None:
            gI.print_simple_line("Weapon: None")
        else:
            gI.print_equipment_info(main_character.get_player_entity().get_weapon())

        if main_character.get_player_entity().get_armor() is None:
            gI.print_simple_line("Armor: None")
        else:
            gI.print_equipment_info(main_character.get_player_entity().get_armor())

        if main_character.get_player_entity().get_accessory() is None:
            gI.print_simple_line("Accessory: None")
        else:
            gI.print_equipment_info(main_character.get_player_entity().get_accessory())

    if x == 2:
        y = 0
        for equip in main_character.backpack:
            gI.print_simple_line("[" + str(y) + "] " + equip.get_name())
            y += 1

    if x == 3:
        y = gI.get_input("Choose a item id from the backpack: ")
        main_character.equip_item(y)

    if x == 4:
        y = gI.get_input("Choose a item id from the backpack: ")
        gI.separator()
        gI.print_equipment_info(main_character.get_backpack_item(y))
    if x == 5:
        return 1
    gI.separator()
    return 3


def main_world():
    gI.print_simple_line("You are at " + wD.get_floor_name(main_character.floor))
    gI.print_simple_menu("Explore,Rest,Manage inventory,Manage skill,See stats,Exit game")
    x = gI.get_input()
    gI.separator()
    if x == 3:
        return 3
    if x == 5:
        return 5
    if x == 6:
        return 0
    gI.print_simple_line("Not implemented yet.")
    gI.separator()


if action == 1:
    plst = characterCreation.character_creation()
    main_character.create_player(plst[0],
                                 plst[1],
                                 plst[2],
                                 plst[3],
                                 plst[4],
                                 plst[5],
                                 plst[6],
                                 plst[7],
                                 plst[8],
                                 plst[9])
    gI.print_player_info(main_character)
    action = 2

if action == 2:
    action = 1
    while action > 0:
        if action == 1:
            action = main_world()
        if action == 3:
            action = manage_inventory()
        if action == 5:
            action = print_player_stats()

