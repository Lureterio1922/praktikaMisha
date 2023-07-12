import numpy as np
import matplotlib.pyplot as plt



# Вычисляем фокусное расстояние
a = 7
b = 3
c = np.sqrt(a**2 - b**2)
import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x и y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# Создаем сетку значений x и y
X, Y = np.meshgrid(x, y)

# Вычисляем значение z в соответствии с уравнением эллиптического цилиндра
Z = (49*(X+9)**2 + 9*(8+Y)**2 - 16)

# Визуализируем эллиптический цилиндр
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=20, cmap='coolwarm')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Эллиптический цилиндр')
plt.grid(True)
plt.show()

# Вычисляем фокусное расстояние
a = 7
b = 3
c = np.sqrt(a**2 - b**2)

# Вычисляем фокусные точки
f1 = (-9 - c, -8)
f2 = (-9 + c, -8)

# Выводим значения фокусных точек в консоль
print("Фокусные точки:")
print("f1 =", f1)
print("f2 =", f2)
# Вычисляем фокусные точки
f1 = (-9 - c, -8)
f2 = (-9 + c, -8)

# Выводим значения фокусных точек в консоль
print("Фокусные точки:")
print("f1 =", f1)
print("f2 =", f2)