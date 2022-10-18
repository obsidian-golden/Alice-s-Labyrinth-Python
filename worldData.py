import random


def get_floor_name(floor_id):
    all_floors = open("Data/Floor_Names.txt", "r")
    result = None
    for floor in all_floors:
        if floor_id == 0:
            result = floor
        floor_id -= 1
    all_floors.close()
    if result is None:
        return "Floor"
    return result.split("|")[0]


def get_random_floor_enemy_encounter(floor_id):
    match floor_id:
        case 1:
            encounters = open("Data/Floors/Beach/Enemy_encounters.txt", "r")
            max_r = 0
            for line in encounters:
                max_r += 1
            target = random.randint(0, max_r)
            for line in encounters:
                if target == 0:
                    result = line
                    break
                target -= 1
            else:
                result = "000|000|000|a"
            encounters.close()
            return result.split("|").pop()
