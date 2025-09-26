import math

def f(x):
    return math.sin(math.pi * x)

def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("No hay cambio de signo en el intervalo.")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Casos de prueba
a1, b1 = -0.5, 2.4  # a + b = 1.9 < 2 → converge a 0
a2, b2 = -0.1, 2.2  # a + b = 2.1 > 2 → converge a 2
a3, b3 = -0.5, 2.5  # a + b = 2 → converge a 1

root1 = bisection(a1, b1)
root2 = bisection(a2, b2)
root3 = bisection(a3, b3)

print(f"Para a + b < 2: converge a {root1:.2f} (debería ser 0)")
print(f"Para a + b > 2: converge a {root2:.2f} (debería ser 2)")
print(f"Para a + b = 2: converge a {root3:.2f} (debería ser 1)")