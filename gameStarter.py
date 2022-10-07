import os

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
