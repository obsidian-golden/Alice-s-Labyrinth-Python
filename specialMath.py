def round_down(number):
    size = len(str(int(number)))
    return int(str(number)[:size])


def in_range(number, maxR=1, minR=0):
    return max(minR, min(maxR, number))
