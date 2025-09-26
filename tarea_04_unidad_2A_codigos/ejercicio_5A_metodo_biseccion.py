def f(x):
    return (x + 3) * (x + 1)**2 * x * (x - 1)**3 * (x - 3)

def biseccion(f, a, b, tolerancia=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print(f"No se puede aplicar el método en el intervalo [{a}, {b}]: f(a) y f(b) deben tener signos opuestos o uno debe ser cero.\n")
        if abs(f(a)) < tolerancia:
            print(f"f({a}) = 0 ⇒ raíz exacta en x = {a}\n")
            return a
        elif abs(f(b)) < tolerancia:
            print(f"f({b}) = 0 ⇒ raíz exacta en x = {b}\n")
            return b
        return None

    for i in range(max_iter):
        p = a + (b - a) / 2
        if abs(f(p)) < tolerancia or abs(b - a) < tolerancia:
            print(f"Iteración {i+1}: raíz aproximada en x = {p:.6f} (f(x) = {f(p):.6f}) en [{a}, {b}]\n")
            return p
        elif f(a) * f(p) < 0:
            b = p
        else:
            a = p

    print("El método no convergió después de", max_iter, "iteraciones.\n")
    return None

# Aplicación a cada intervalo
intervalos = [
    ("a", -1.5, 2.5),
    ("b", -0.5, 2.4),
    ("c", -0.5, 3),
    ("d", -3, -0.5),
]

print("Aplicando el método de bisección a cada intervalo:\n")
for etiqueta, a, b in intervalos:
    print(f"Intervalo {etiqueta}: [{a}, {b}]")
    biseccion(f, a, b)
