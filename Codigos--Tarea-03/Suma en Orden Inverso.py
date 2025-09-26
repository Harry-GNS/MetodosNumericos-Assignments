# Ubicación: Discusión del Ejercicio 1 (Suma de series en orden inverso).
# Propósito: Sumar una lista de números desde el último elemento hasta el primero.

def sumar_en_orden_inverso(n, lista):
    # Paso 1: Inicializamos la suma en 0
    suma = 0    
    # Paso 2: Recorremos la lista desde el final hasta el principio
    for i in range(n-1, -1, -1):
        suma += lista[i]  # Sumamos el valor de x_i    
    # Paso 3: Retornamos el resultado de la suma
    return suma

# Ejemplo de uso
n = 4
valores = [1, 2, 3, 4]  # x1 = 1, x2 = 2, x3 = 3, x4 = 4
# Llamamos a la función
resultado = sumar_en_orden_inverso(n, valores)
print(f"La suma en orden inverso es: {resultado}")