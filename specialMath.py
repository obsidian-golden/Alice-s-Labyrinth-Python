def round_down(number):
    size = len(str(int(number)))
    return str(number)[:size]


def in_range(number, maxR = 1, minR = 0):
    return min(minR, max(maxR, number))
