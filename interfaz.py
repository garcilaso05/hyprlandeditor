import os
import json
import tkinter as tk
from tkinter import colorchooser, messagebox


# Editor de la interfaz de las ventanas de hyprland
# Bordes: color, degradado, ancho...

class ConfigEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de configuración Hyprland")

        
        
        # Rutas de archivos (cambiar nombre de usuario si es necesario [path absoluto])

        self.config_path = "$HOME/.config/hypr/hyprland.conf"
        self.state_file = "$HOME/.config/hyprland_editor_state.json"
        
        # Variables de configuración con valores predeterminados
        self.default_state = {
            "t_borde": 1,
            "c_arriba": "000000aa",
            "c_abajo": "000000aa",
            "c_inactivo": "000000aa",
            "redondeado": 0
        }
        self.state = self.load_state()
        
        # Variables de Tkinter
        self.t_borde = tk.IntVar(value=self.state["t_borde"])
        self.c_arriba = tk.StringVar(value=self.state["c_arriba"])
        self.c_abajo = tk.StringVar(value=self.state["c_abajo"])
        self.c_inactivo = tk.StringVar(value=self.state["c_inactivo"])
        self.redondeado = tk.IntVar(value=self.state["redondeado"])
        
        # Crear la interfaz
        self.create_interface()
        
    
    def create_interface(self):
        
        tk.Label(self.root, text="Tamaño del borde (1-5):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Scale(self.root, from_=1, to=5, orient="horizontal", variable=self.t_borde).grid(row=0, column=1, pady=5)

        tk.Label(self.root, text="Color arriba (hex):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Button(self.root, text="Seleccionar", command=lambda: self.pick_color(self.c_arriba)).grid(row=1, column=1, pady=5)
        tk.Entry(self.root, textvariable=self.c_arriba, width=10).grid(row=1, column=2, padx=5)

        tk.Label(self.root, text="Color abajo (hex):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Button(self.root, text="Seleccionar", command=lambda: self.pick_color(self.c_abajo)).grid(row=2, column=1, pady=5)
        tk.Entry(self.root, textvariable=self.c_abajo, width=10).grid(row=2, column=2, padx=5)

        tk.Label(self.root, text="Color inactivo (hex):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Button(self.root, text="Seleccionar", command=lambda: self.pick_color(self.c_inactivo)).grid(row=3, column=1, pady=5)
        tk.Entry(self.root, textvariable=self.c_inactivo, width=10).grid(row=3, column=2, padx=5)

        tk.Label(self.root, text="Redondeado (0-10):").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        tk.Scale(self.root, from_=0, to=10, orient="horizontal", variable=self.redondeado).grid(row=4, column=1, pady=5)

        tk.Button(self.root, text="Guardar configuración", command=self.save_config).grid(row=5, column=0, columnspan=3, pady=10)

    def pick_color(self, color_var):
        color_code = colorchooser.askcolor(title="Selecciona un color")[1]
        if color_code:
            color_var.set(color_code[1:] + "aa")  # Convertir a formato hex con "aa" final

    def save_config(self):
        if not os.path.exists(self.config_path):
            messagebox.showerror("Error", f"Archivo de configuración no encontrado: {self.config_path}")
            return

        # Validar colores
        for color_var in [self.c_arriba, self.c_abajo, self.c_inactivo]:
            if not self.validate_color(color_var.get()):
                messagebox.showerror("Error", f"Color inválido: {color_var.get()}")
                return

        # Leer archivo y modificar las líneas relevantes
        try:
            with open(self.config_path, "r") as file:
                lines = file.readlines()

            # Modificar las primeras líneas según las variables
            lines[0] = f"$t_borde = {self.t_borde.get()}\n"
            lines[1] = f"$c_arriba = {self.c_arriba.get()}\n"
            lines[2] = f"$c_abajo = {self.c_abajo.get()}\n"
            lines[3] = f"$c_inactivo = {self.c_inactivo.get()}\n"
            lines[4] = f"$redondeado = {self.redondeado.get()}\n"

            with open(self.config_path, "w") as file:
                file.writelines(lines)

            # Guardar el estado en el archivo de soporte
            self.save_state()

            messagebox.showinfo("Éxito", "Configuración guardada exitosamente.")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la configuración: {e}")

    def load_state(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                pass  # Si el archivo está corrupto, usar los valores predeterminados
        return self.default_state

    def save_state(self):
        state = {
            "t_borde": self.t_borde.get(),
            "c_arriba": self.c_arriba.get(),
            "c_abajo": self.c_abajo.get(),
            "c_inactivo": self.c_inactivo.get(),
            "redondeado": self.redondeado.get()
        }
        try:
            with open(self.state_file, "w") as file:
                json.dump(state, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el estado: {e}")

    @staticmethod
    def validate_color(color):
        return len(color) == 8 and all(c in "0123456789abcdefABCDEF" for c in color)


# Crear ventana de la aplicación
root = tk.Tk()
app = ConfigEditor(root)
root.mainloop()