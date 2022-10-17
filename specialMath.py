def round_down(number):
    return int(str(number).split(".")[0])


def clamp(number, minR, maxR):
    return max(minR, min(maxR, number))


def in_range(number, maxR, minR):
    if maxR >= number >= minR:
        return True
    else:
        return False


def real_element_state(x, y):
    return int(((3 * x) + y)/4)


def get_main_original_type_from_real(x):
    if 0 <= x <= 4:
        return 0
    if 5 <= x <= 9:
        return 1
    if 10 <= x <= 14:
        return 2
    if 15 <= x <= 19:
        return 3
    if 20 <= x <= 24:
        return 4


def get_sub_original_type_from_real(x):
    if 0 <= x <= 4:
        return x
    if 5 <= x <= 9:
        return x - 5
    if 10 <= x <= 14:
        return x - 10
    if 15 <= x <= 19:
        return x - 15
    if 20 <= x <= 24:
        return x - 20
