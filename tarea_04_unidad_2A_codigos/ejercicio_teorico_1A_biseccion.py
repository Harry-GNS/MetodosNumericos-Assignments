import math

def f(x):
    return x**3 - x - 1

def bisection(a, b, tol, max_iter):
    iter_count = 0
    while (b - a) >= tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return (a + b) / 2, iter_count

# Parámetros
a, b = 1, 2
tol = 1e-4
max_iter = 14  # Según el teorema

root, iterations = bisection(a, b, tol, max_iter)
print(f"Aproximación de la raíz: {root:.6f}")
print(f"Número de iteraciones: {iterations}")