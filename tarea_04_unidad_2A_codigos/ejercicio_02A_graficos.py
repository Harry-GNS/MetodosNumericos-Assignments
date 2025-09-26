import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de x
x = np.linspace(0, 2*np.pi, 1000)
y1 = x
y2 = np.sin(x)

# Crear la gráfica
plt.plot(x, y1, label='y = x', color='blue')
plt.plot(x, y2, label='y = sin(x)', color='red')

# Añadir detalles
plt.title('Gráficas de y = x y y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

