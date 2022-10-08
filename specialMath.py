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
