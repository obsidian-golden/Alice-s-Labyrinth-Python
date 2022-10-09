import gameInterface as gI


def character_creation():
    gI.separator()
    gI.print_simple_line("---Character creation---")
    # name="", body=1, soul=1, mind=1, hp_b=5, empty=0, earth=0, water=0, energy=0, life=0
    tp = ["", 1, 1, 1, 5, 0, 0, 0, 0, 0]
    ele = ["empty", "earth", "water", "energy", "life"]
    prm = 3
    while prm > 0:
        gI.print_simple_line("Elemental affinities")
        gI.print_simple_menu("Empty,Earth,Water,Energy,Life")
        option = int(gI.get_input())
        if 1 <= option <= 5:
            tp[option + 4] += 1
            prm -= 1
            gI.print_simple_line("Increased affinity with the " + ele[option-1] + " element.")
        else:
            gI.print_simple_line("Invalid input")
        gI.separator()
        if prm <= 0:
            gI.print_simple_line("Current elemental affinities")
            for x in range(5):
                if tp[x+5] > 0:
                    print(ele[x] + " = [" + str(tp[x+5]) + "]")
            gI.print_simple_menu("Confirm,Choose again")
            option = int(gI.get_input())
            if option == 2:
                prm = 3
                for x in range(5):
                    tp[x + 5] = 0
            gI.separator()
    prm = 1
    while prm == 1:
        tp[0] = str(gI.get_input("Choose a name: "))
        gI.separator()
        gI.print_simple_line("Your name is: " + str(tp[0]))
        gI.print_simple_menu("Confirm,Choose again")
        option = int(gI.get_input())
        if option == 1:
            prm = 0
        gI.separator()
    gI.print_simple_line("Character creation complete")
    gI.separator()
    return tp
