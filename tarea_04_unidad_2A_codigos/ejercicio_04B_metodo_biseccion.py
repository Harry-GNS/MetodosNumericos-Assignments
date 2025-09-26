import math

def f(x):
    return x**2 - 1 - math.exp(1 - x**2)

def biseccion(f, a, b, tolerancia=1e-3, max_iter=100):
    if f(a) * f(b) >= 0:
        print(f"No se puede aplicar el método en el intervalo [{a}, {b}]: f(a) y f(b) deben tener signos opuestos.\n")
        return None

    for i in range(max_iter):
        p = a + (b - a) / 2
        if abs(f(p)) < tolerancia or abs(b - a) < tolerancia:
            print(f"Iteración {i+1}: raíz aproximada en x = {p:.5f} (f(x) = {f(p):.5f})\n")
            return p
        elif f(a) * f(p) < 0:
            b = p
        else:
            a = p

    print("El método no convergió después de", max_iter, "iteraciones.\n")
    return None

# Aplicar el método de bisección en [-2, 0]
print("Resolviendo x² - 1 = e^(1 - x²) usando bisección:")
biseccion(f, -2, 0)
