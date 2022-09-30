def round_down(number):
    return int(str(number).split(".")[0])


def in_range(number, maxR=1, minR=0):
    return max(minR, min(maxR, number))
