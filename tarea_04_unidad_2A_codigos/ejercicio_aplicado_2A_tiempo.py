import math

def f(t):
    return 300 - 24.525 * t + 61.3125 * (1 - math.exp(-0.4 * t))

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No hay cambio de signo en el intervalo.")
        return None
    c = a
    while (b - a) >= tol:
        c = (a + b) / 2
        if abs(f(c)) < 1e-10:  # Evita comparar con 0 directamente
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

# Intervalo inicial [0, 20] y tolerancia 0.01
t_solution = bisection(0, 20, 0.01)
print(f"El tiempo que tarda en golpear el piso es: {t_solution:.2f} segundos")
