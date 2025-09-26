import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

class InterfazInteractiva:
    def __init__(self, master, radios):
        self.master = master
        self.radios = radios
        master.title("Simulación Interactiva")

        # Configuración inicial de los círculos
        self.centros = {
            'c1': {'x': 2, 'y': 2, 'radio': radios['r1'], 'arrastrando': False},
            'c2': {'x': 5, 'y': 5, 'radio': radios['r2'], 'arrastrando': False},
            'c3': {'x': 8, 'y': 3, 'radio': radios['r3'], 'arrastrando': False}
        }

        # Crear figura matplotlib
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Almacenar los objetos gráficos
        self.circulos = {}
        self.lineas_tangentes = []
        self.textos = {}

        # Configurar eventos
        self.canvas.mpl_connect('button_press_event', self.al_presionar)
        self.canvas.mpl_connect('button_release_event', self.al_soltar)
        self.canvas.mpl_connect('motion_notify_event', self.al_arrastrar)

        self.inicializar_graficos()

    def inicializar_graficos(self):
        self.ax.clear()
        self.ax.set_xlim(-5, 15)
        self.ax.set_ylim(-5, 15)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        # Dibujar círculos
        colores = ['red', 'blue', 'green']
        for i, (key, circ) in enumerate(self.centros.items()):
            self.circulos[key] = Circle(
                (circ['x'], circ['y']), circ['radio'],
                color=colores[i], alpha=0.3, label=f'C{i+1}')
            self.ax.add_patch(self.circulos[key])
            self.ax.plot(circ['x'], circ['y'], 'k.', markersize=4)
            self.textos[key] = self.ax.text(
                circ['x'], circ['y'], f"C{i+1}", 
                ha='center', va='center', fontsize=8)

        # Dibujar tangentes
        self.actualizar_tangentes()
        self.canvas.draw()

    def actualizar_tangentes(self):
        # Eliminar líneas antiguas
        for linea in self.lineas_tangentes:
            linea.remove()
        self.lineas_tangentes = []

        # Dibujar nuevas tangentes
        pares = [('c1', 'c2'), ('c2', 'c3'), ('c1', 'c3')]
        for a, b in pares:
            tangentes = self.calcular_tangentes_externas(self.centros[a], self.centros[b])
            for p1, p2 in tangentes:
                linea = Line2D([p1[0], p2[0]], [p1[1], p2[1]], color='cyan', lw=1)
                self.ax.add_line(linea)
                self.lineas_tangentes.append(linea)

    def calcular_tangentes_externas(self, c1, c2):
        # (Mantén el mismo código que tenías para calcular tangentes)
        x1, y1, r1 = c1['x'], c1['y'], c1['radio']
        x2, y2, r2 = c2['x'], c2['y'], c2['radio']

        dx = x2 - x1
        dy = y2 - y1
        d = np.hypot(dx, dy)

        if d < abs(r1 - r2) or d == 0:
            return []

        vx = dx / d
        vy = dy / d

        res = []
        for sign in [+1, -1]:
            h = (r2 - r1) / d
            if abs(h) > 1:
                continue
            a = np.arccos(h)
            sin_a = np.sin(a)
            cos_a = np.cos(a)

            tx = vx * cos_a - sign * vy * sin_a
            ty = vy * cos_a + sign * vx * sin_a

            p1 = (x1 + r1 * tx, y1 + r1 * ty)
            p2 = (x2 + r2 * tx, y2 + r2 * ty)
            res.append((p1, p2))
        return res

    def al_presionar(self, event):
        if event.inaxes != self.ax or event.xdata is None or event.ydata is None:
            return

        for key, circ in self.centros.items():
            distancia = np.hypot(event.xdata - circ['x'], event.ydata - circ['y'])
            if distancia <= circ['radio']:
                circ['arrastrando'] = True
                circ['offset_x'] = circ['x'] - event.xdata
                circ['offset_y'] = circ['y'] - event.ydata
                break

    def al_arrastrar(self, event):
        if event.inaxes != self.ax or event.xdata is None or event.ydata is None:
            return

        for key, circ in self.centros.items():
            if circ.get('arrastrando', False):
                # Actualizar posición
                circ['x'] = event.xdata + circ.get('offset_x', 0)
                circ['y'] = event.ydata + circ.get('offset_y', 0)
                
                # Actualizar gráficos
                self.circulos[key].center = (circ['x'], circ['y'])
                self.textos[key].set_position((circ['x'], circ['y']))
                self.actualizar_tangentes()
                
                self.canvas.draw()
                break

    def al_soltar(self, event):
        for key, circ in self.centros.items():
            circ['arrastrando'] = False
            circ.pop('offset_x', None)
            circ.pop('offset_y', None)