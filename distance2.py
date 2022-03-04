from math import sqrt


def distances(x1, x2, y1, y2):
    distance = sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)
    return distance


print(distances(1, 2, 2, 4))
