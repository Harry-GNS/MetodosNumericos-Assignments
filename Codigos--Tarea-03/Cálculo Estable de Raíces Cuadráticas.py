#Ubicación: Discusión del Ejercicio 2 (Raíces de ecuaciones cuadráticas).
# Propósito: Calcular raíces de  evitando cancelación numérica

import cmath

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c
    raiz_d = cmath.sqrt(discriminante)

    if b != 0:
        q = -0.5 * (b + (1 if b > 0 else -1) * raiz_d)
        x1 = q / a
        x2 = c / q
    else:
        x1 = (-b + raiz_d) / (2*a)
        x2 = (-b - raiz_d) / (2*a)

    return x1, x2

# Ejemplo de uso
a, b, c = 1, -5, 6  # x^2 - 5x + 6 = 0 → raíces: 3 y 2
x1, x2 = calcular_raices(a, b, c)
print(f"Raíces: x1 = {x1}, x2 = {x2}")

