import tkinter as tk
from tkinter import ttk, messagebox
from utils import calcular_promedio, ordenar_descendente


class ExpensasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Expensas")

        self.unidades = []
        self.superficies = []
        self.gastos = []

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Número de unidad:").grid(
            row=0, column=0, padx=5, pady=5)
        self.unidad_entry = tk.Entry(self.root)
        self.unidad_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Superficie (m²):").grid(
            row=1, column=0, padx=5, pady=5)
        self.superficie_entry = tk.Entry(self.root)
        self.superficie_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Agregar unidad", command=self.agregar_unidad).grid(
            row=2, column=0, columnspan=2, pady=5)

        tk.Label(self.root, text="Valor del m²:").grid(
            row=3, column=0, padx=5, pady=5)
        self.valor_m2_entry = tk.Entry(self.root)
        self.valor_m2_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Calcular", command=self.calcular).grid(
            row=4, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=(
            "unidad", "superficie", "gasto"), show="headings")
        self.tree.heading("unidad", text="Unidad")
        self.tree.heading("superficie", text="Superficie (m²)")
        self.tree.heading("gasto", text="Gasto ($)")
        self.tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.promedio_label = tk.Label(
            self.root, text="Promedio general: $0.00")
        self.promedio_label.grid(row=6, column=0, columnspan=2, pady=10)

    def agregar_unidad(self):
        try:
            nro = int(self.unidad_entry.get())
            sup = float(self.superficie_entry.get())

            if nro in self.unidades:
                messagebox.showerror("Error", "Unidad ya ingresada.")
                return
            if sup <= 0:
                messagebox.showerror(
                    "Error", "La superficie debe ser mayor a cero.")
                return

            self.unidades.append(nro)
            self.superficies.append(sup)

            self.tree.insert("", "end", values=(nro, f"{sup:.2f}", "-"))

            self.unidad_entry.delete(0, tk.END)
            self.superficie_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Datos inválidos.")

    def calcular(self):
        try:
            valor_m2 = float(self.valor_m2_entry.get())
            if valor_m2 <= 0:
                raise ValueError

            # Usamos tu calcular_promedio que también devuelve lista_gastos
            promedio, self.gastos = calcular_promedio(
                self.superficies, valor_m2)

            # Ordenamos usando tu función
            self.unidades, self.superficies, self.gastos = ordenar_descendente(
                self.unidades, self.superficies, self.gastos
            )

            # Limpiar tabla
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Mostrar resultados
            for i in range(len(self.unidades)):
                self.tree.insert("", "end", values=(
                    self.unidades[i],
                    f"{self.superficies[i]:.2f}",
                    f"${self.gastos[i]:.2f}"
                ))

            self.promedio_label.config(
                text=f"Promedio general: ${promedio:.2f}")

        except ValueError:
            messagebox.showerror(
                "Error", "Ingrese un valor válido para el metro cuadrado.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpensasApp(root)
    root.mainloop()
