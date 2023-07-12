import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функция для построения астроиды
def plot_astroid():
    t = np.linspace(0, 2*np.pi, 1000)
    x = 6 * (np.cos(t) + (np.cos(6*t))/6)
    y = 6 * (np.sin(t) - (np.sin(6*t))/6)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Семиконечная астроида')
    plt.grid(True)
    plt.show()

# Функция для вычисления площади астроиды
def calculate_area():
    def integrand(t):
        return (6 * (np.cos(t) + (np.cos(6*t))/6))**2

    area, error = quad(integrand, 0, 2*np.pi)
    return area

# Вызываем функции для построения астроиды и вычисления площади
plot_astroid()
area = calculate_area()
print("Площадь астроиды равна:", area)