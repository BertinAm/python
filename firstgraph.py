import numpy as np
from matplotlib import pyplot as plt
import numpy as np


def found_fit(x):
    return 0.388 * x ** 2


x_data = list(range(10))
y_data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
x_func = np.linspace(0, 10, 50)
y_func = found_fit(x_func)
plt.scatter(x_data, y_data, c="r", label='data')
plt.plot(x_func, y_func, label='$f(x) = 0.388 x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting primes')
plt.legend()
print(plt.show())
