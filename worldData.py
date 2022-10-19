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


def get_max_floor_encounters(floor_id):
    f_name = get_floor_name(floor_id)
    data = open("Data/Floors/" + f_name + "/Extra_data.txt")
    for line in data:
        x = line.split("|")[0]
        break
    return int(x)


def get_random_floor_enemy_encounter(floor_id):
    match floor_id:
        case 1:
            encounters = open("Data/Floors/Beach/Enemy_encounters.txt", "r")
            max_r = get_max_floor_encounters(floor_id) - 1
            target = random.randint(0, max_r)
            result = None
            for line in encounters:
                if target == 0:
                    result = line
                    break
                target -= 1
            if result is None:
                result = "001|000|000|"
            encounters.close()
            result_list = result.split("|")
            result_list.pop()
            return result_list
