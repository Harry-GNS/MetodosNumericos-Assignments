import tkinter as tk
from tkinter import ttk

class InterfazEntrada:
    def __init__(self, master):
        self.master = master
        master.title("Configuración Inicial")
        master.geometry("300x200")
        
        tk.Label(master, text="Ingrese los radios de los círculos", font=('Arial', 12)).pack(pady=10)
        
        self.radios = {}
        for i in range(1, 4):
            frame = ttk.Frame(master)
            frame.pack(pady=5)
            tk.Label(frame, text=f"Radio C{i}:").pack(side=tk.LEFT)
            self.radios[f"r{i}"] = tk.Entry(frame, width=10)
            self.radios[f"r{i}"].pack(side=tk.LEFT)
            self.radios[f"r{i}"].insert(0, str(i+1))  # Valores por defecto
        
        ttk.Button(master, text="Continuar", command=self.continuar).pack(pady=20)

    def continuar(self):
        try:
            radios = {f"r{i}": float(self.radios[f"r{i}"].get()) for i in range(1, 4)}
            self.master.destroy()  # Cierra esta ventana
            from interfaz_interactiva import InterfazInteractiva
            root = tk.Tk()
            InterfazInteractiva(root, radios)
            root.mainloop()
        except ValueError:
            tk.messagebox.showerror("Error", "Los radios deben ser números positivos")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazEntrada(root)
    root.mainloop()