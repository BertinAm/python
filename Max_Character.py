from statistics import mode  # statistics module that provides methods like the mode, median, mean etc


def most_common(lits):  # function definition
    common = mode(lits)
    return common


print(most_common(["c", "d", "t", "c", "c", "r"]))  # calling of the function most_common
