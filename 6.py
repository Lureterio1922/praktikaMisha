from scipy.integrate import quad

def integrand(x):
    return 12*x**5 + x**2

result, error = quad(integrand, 1, 15)
print("Значение интеграла:", result)