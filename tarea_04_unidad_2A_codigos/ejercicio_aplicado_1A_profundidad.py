import math

def f(h):
    return 0.5 * math.pi - math.asin(h) - h * math.sqrt(1 - h**2) - 1.24

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No hay cambio de signo en el intervalo.")
        return None
    c = a
    while (b - a) >= tol:
        c = (a + b) / 2
        if abs(f(c)) < 1e-10:  # Evita comparar con 0 directamente por posibles errores numéricos
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

# Intervalo inicial [0, 1] y tolerancia 0.01
h_solution = bisection(0, 1, 0.01)
print(f"La profundidad del agua es: {h_solution:.3f} cm")