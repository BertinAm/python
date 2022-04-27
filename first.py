import numpy as np

a = np.array([230, 10, 284, 39, 76])  # creating a numpy array
cutoff = 100  # setting a limiting value
new_a = []
for x in a:
    if x < cutoff:
        new_a.append(x * 2)
    else:
        new_a.append(x)
for new in new_a:
    if 150 < new < 200:
        a = np.array(new)  # limiting the values to only elements within the range 150 to 200
        print(a)
