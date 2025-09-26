import math

def f(x):
    return x - math.tan(x)

def biseccion(f, a, b, tolerancia=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print(f"No se puede aplicar el método en el intervalo [{a}, {b}]: f(a) y f(b) deben tener signos opuestos.\n")
        return None

    for i in range(max_iter):
        p = a + (b - a) / 2
        if abs(f(p)) < tolerancia or abs(b - a) < tolerancia:
            print(f"Iteración {i+1}: raíz aproximada en x = {p:.6f} (f(x) = {f(p):.6f})\n")
            return p
        elif f(a) * f(p) < 0:
            b = p
        else:
            a = p

    print("El método no convergió después de", max_iter, "iteraciones.\n")
    return None

# Buscar la raíz en un intervalo antes de pi/2
print("Resolviendo x = tan(x) usando bisección:")
biseccion(f, -0.5, 1.4)
