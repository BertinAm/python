def distances(x1, x2, y1, y2):
    value1 = x2 - x1
    value2 = y2 - y1
    value_squared = (value1 ** 2) + (value2 ** 2)
    distance = value_squared ** 0.5
    return distance


print(distances(1, 2, 2, 4))
