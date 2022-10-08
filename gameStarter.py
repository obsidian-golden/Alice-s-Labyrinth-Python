import player
import entities

separator = "-----"
state = 0
action = 0

while state == 0:
    print("[1]Start new game")
    print("[2]Load game")
    print("[3]exit")
    action = input("Choose a option: ")
    if action == 3:
        state = -1
    if action == 2:
        print(separator)
        print("not supported yet")
    if action == 1:
        state = 1
    print(separator)
    action = 0

if state == 1:
    print("Character creation")
    stp = {"name": "",
           "body": 1,
           "soul": 1,
           "mind": 1,
           "hp_b": 5,
           "empty": 0,
           "earth": 0,
           "water": 0,
           "energy": 0,
           "life": 0
           }
    print(separator)
    rep = 3
    elem = ["empty", "earth", "water", "energy", "life"]
    while rep > 0:
        print(str(rep) + " points remaining")
        print("Choose elemental affinities: ")
        print("[0]empty")
        print("[1]earth")
        print("[2]water")
        print("[3]energy")
        print("[4]life")
        inp = int(input("Choose a option: "))
        if 0 <= inp <= 4:
            stp[elem[inp]] += 1
            print("The " + elem[inp] + " affinity has increased")
            rep -= 1
        else:
            print(separator)
            print("Invalid choice")
        print(separator)
        if rep <= 0:
            print("Affinity levels:")
            for x in elem:
                print(x + " level is " + str(stp[x]))
            print("[1] confirm")
            print("[2] reset")
            inp = int(input("Choose a option: "))
            print(separator)
            if inp == 2:
                rep = 3
                for x in elem:
                    stp[x] = 0
    stp["name"] = input("Choose your name: ")
    print(separator)
    player.player_entity = entities.BaseEntity(stp["name"],
                                               stp["body"],
                                               stp["soul"],
                                               stp["mind"],
                                               stp["hp_b"],
                                               stp["empty"],
                                               stp["earth"],
                                               stp["water"],
                                               stp["energy"],
                                               stp["life"])
    print("Player creation has been completed")
    player.print_player_info()
    print(separator)
