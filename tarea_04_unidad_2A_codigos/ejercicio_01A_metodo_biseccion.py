def f(x):
 return x**3 - 7*x**2 + 14*x - 6

def biseccion(f, a, b, tolerancia=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print(f"No se puede aplicar el método en el intervalo [{a}, {b}]: f(a) y f(b) deben tener signos opuestos.\n")
        return None

    for i in range(max_iter):
        p = a + (b - a) / 2
        if abs(f(p)) < tolerancia or abs(b - a) < tolerancia:
            print(f"Iteración {i+1}: raíz aproximada en x = {p:.6f} para intervalo [{a}, {b}]\n")
            return p
        elif f(a) * f(p) < 0:
            b = p
        else:
            a = p

    print("El método no convergió después de", max_iter, "iteraciones.\n")
    return None

# Aplicar el método a cada intervalo
print("a. Intervalo [0, 1]")
biseccion(f, 0, 1)

print("b. Intervalo [1, 3.2]")
biseccion(f, 1, 3.2)

print("c. Intervalo [3.2, 4]")
biseccion(f, 3.2, 4)

