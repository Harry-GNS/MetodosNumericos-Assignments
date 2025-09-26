import numpy as np
import matplotlib.pyplot as plt

# Valores de x en el intervalo [-2, 2]
x = np.linspace(-2, 2, 400)
y1 = x**2 - 1
y2 = np.exp(1 - x**2)

# Graficar ambas funciones
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='y = x² - 1', color='blue')
plt.plot(x, y2, label='y = e^(1 - x²)', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráficas de y = x² - 1 y y = e^(1 - x²)')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
