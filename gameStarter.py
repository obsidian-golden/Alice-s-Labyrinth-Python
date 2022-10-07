state = 0
action = 0
while state == 0:
    print("[1]Start new game")
    print("[2]Load game")
    print("[3]exit")
    action = input("Choose a option: ")
    print("-----")
    if action == 3:
        state = -1
    if action == 2:
        print("not supported yet")
    if action == 1:
        print("not supported yet")
    print("-----")
    action = 0

if state == 1:
    stp = {"name": "",
           "body": 1,
           "soul": 1,
           "mind": 1,
           "hp_b": 5,
           "level": 1,
           "none": 1,
           "earth": 1,
           "water": 1,
           "energy": 1,
           "life": 1,
           "c_class": 0
           }
    print("Base stats: body = 1, soul = 1, mind = 1, base health = 5")
    print("Base elemental stats: none = 1, earth = 1, water = 1, energy = 1, life = 1")
    print("Choose a species:")
    print("[1]Human: base health = 7, life = 2")
