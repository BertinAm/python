def register_check(dec):
    count = 0
    dec1 = dec.values()
    dec2 = list(dec1)
    return "The number of Students in school are : ", dec2.count('yes')


print(register_check(dec={'Micheal': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}))
