#Ubicación: Discusión del Ejercicio 3 (Serie infinita y error absoluto).
#Propósito: Encontrar el número mínimo de términos para que una serie converja con error absoluto 

def calcular_numero_de_terminos(x, epsilon=1e-6):
    def f_exacta(x):
        return (1 + 2*x) / (1 + x + x**2)

    exacto = f_exacta(x)
    S = 0
    k = 0
    error = float('inf')

    while error > epsilon:
        num = (2**k) * x**(2**k - 1) * (1 - 2*x)
        den = 1 - x**(2**k) + x**(2**(k+1))
        Tk = num / den
        S += Tk
        error = abs(S - exacto)
        k += 1

    return k, S, exacto

# Ejemplo con x = 0.25
terminos, aproximacion, valor_real = calcular_numero_de_terminos(0.25)
print(f"Número de términos requeridos: {terminos}")
print(f"Valor aproximado: {aproximacion}")
print(f"Valor exacto: {valor_real}")