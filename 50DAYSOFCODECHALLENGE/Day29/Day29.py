# Day29: 50daysofcodechallenge
def middle_figure(a, b):
    try:
        import statistics as stats
        c = a + " " + b
        c = c.replace(" ", "")
        empty = [d for d in c]
        new = []
        for index, letter in enumerate(empty):
            new.append(index)
        median = stats.median(new)
        return empty[median]
    except TypeError:
        return "no middle figure"


print(middle_figure(input("enter first phrase \n"), input("Enter second phrase \n")))
