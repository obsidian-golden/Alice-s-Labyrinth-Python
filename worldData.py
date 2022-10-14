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

