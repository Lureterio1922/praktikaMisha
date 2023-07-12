import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Построение графиков функций
x = np.linspace(0, 2, 100)
y1 = 2*x - x**2
y2 = 4*x - 2*x**2

plt.plot(x, y1, label='y=2x-x^2')
plt.plot(x, y2, label='y=4x-2x^2')
plt.fill_between(x, y1, y2, where=(y1>y2), color='gray', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Вычисление объема тела
def integrand(x):
    return np.pi * (y2**2 - y1**2)

volume, error = quad(integrand, 0, 2)
print("Объем тела, образованного вращением этой площади вокруг оси OX, равен:", volume)