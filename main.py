import gameInterface as gI
import characterCreation
import player

gI.print_simple_menu("Start game,Exit")
action = int(gI.get_input())

main_character = player.Player()


def main_world():
    return 0


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
    gI.separator()
    action = 2

if action == 2:
    action = 1
    while action > 0:
        if action == 1:
            action = main_world()
