# Day30: 50daysofcodechallenge
def repeated_name(name):
    import collections

    cc = collections.Counter(name)
    for c in name:
        if cc[c] > 1:
            num = max(cc.values())
            for key, values in cc.items():
                if num == values:
                    return key
            break


l = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(l))
