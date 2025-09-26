import numpy as np
import matplotlib.pyplot as plt

# Rango de valores para x evitando las asíntotas de tan(x)
x = np.linspace(-1.5*np.pi, 1.5*np.pi, 1000)
x = x[np.abs(np.cos(x)) > 0.01]  # Eliminar puntos donde cos(x) ~ 0 para evitar valores extremos

y1 = x
y2 = np.tan(x)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = x', color='blue')
plt.plot(x, y2, label='y = tan(x)', color='orange')

# Dibujar líneas verticales para las asíntotas de tan(x)
for k in range(-2, 3):
    asintota = (np.pi/2) + k * np.pi
    plt.axvline(asintota, color='gray', linestyle='--', linewidth=0.7)

plt.title('Gráficas de y = x y y = tan(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-10, 10)  # Limitar el eje y para evitar saltos grandes en la tangente
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
