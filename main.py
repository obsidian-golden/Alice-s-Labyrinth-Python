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
    x = int(gI.get_input())
    gI.separator()
    match x:
        case 1:
            gI.print_simple_line("Player equipment: ")
            if main_character.get_player_entity().get_weapon() is None:
                gI.print_simple_line("Weapon: None")
            else:
                gI.print_equipment_info(main_character.get_player_entity().get_weapon())

            gI.print_simple_line("-")

            if main_character.get_player_entity().get_armor() is None:
                gI.print_simple_line("Armor: None")
            else:
                gI.print_equipment_info(main_character.get_player_entity().get_armor())

            gI.print_simple_line("-")

            if main_character.get_player_entity().get_accessory() is None:
                gI.print_simple_line("Accessory: None")
            else:
                gI.print_equipment_info(main_character.get_player_entity().get_accessory())

            gI.print_simple_line("-")

        case 2:
            y = 0
            for equip in main_character.backpack:
                gI.print_simple_line("[" + str(y) + "] " + equip.get_name())
                y += 1

        case 3:
            y = int(gI.get_input("Choose a item id from the backpack: "))
            main_character.equip_item(y)

        case 4:
            y = int(gI.get_input("Choose a item id from the backpack: "))
            gI.separator()
            gI.print_equipment_info(main_character.get_backpack_item(y))
        case 5:
            return 1
        case _:
            gI.print_simple_line("Invalid choice")
    gI.separator()
    return 2


def main_world():
    gI.print_simple_line("You are at " + wD.get_floor_name(main_character.floor))
    gI.print_simple_menu("Explore,Manage inventory,Manage skill,See stats,Exit game")
    x = int(gI.get_input())

    gI.separator()
    match x:
        case 2:
            return 2
        case 4:
            return 4
        case 5:
            return 0
        case _:
            gI.print_simple_line("Not implemented yet.")
            gI.separator()
            return 1


if action == 1:
    while not main_character.player_exist:
        plst = characterCreation.character_creation()
        main_character.create_player(plst)
        if not main_character.player_exist:
            gI.print_simple_line("Character creation failed")
    gI.print_simple_line("Character creation success")
    gI.print_player_info(main_character)
    action = 2

if action == 2:
    action = 1
    while action > 0:
        match action:
            case 1:
                action = main_world()
            case 2:
                action = manage_inventory()
            case 4:
                action = print_player_stats()
            case _:
                action = 1

