import numpy as np
import matplotlib.pyplot as plt


def f(x):# Определение функции
    return np.cbrt(np.sin(x) + 6)

x = np.linspace(-10, 10, 100)# Создание массива значений x
y = f(x)# Вычисление значений функции для каждого значения x

# Построение графика
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) = ∛(sin(x) + 6)')
plt.grid(True)
plt.show()