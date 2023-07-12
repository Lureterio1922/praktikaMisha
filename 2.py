import numpy as np

# Создание матрицы коэффициентов
A = np.array([[1, -1, 1],
              [0, 1, -1],
              [0, 1, -3]])

# Создание вектора свободных членов
B = np.array([2, -1, -5])

# Решение уравнения
solution = np.linalg.solve(A, B)

# Вывод решения
print("Решение уравнения:")
print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])