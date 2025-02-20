import os
import json
import tkinter as tk
from tkinter import colorchooser, messagebox
from pathlib import Path


# Editor de la interfaz de las ventanas de hyprland
# Bordes: color, degradado, ancho...

class ConfigEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de configuración Hyprland")

        
        
        # Rutas de archivos (cambiar nombre de usuario si es necesario [path absoluto])

        self.config_path = Path("~/.config/hypr/hyprland.conf").expanduser()
        
        # Variables de configuración con valores predeterminados
        self.default_state = {
            "t_borde": 1,
            "c_arriba": "000000aa",
            "c_abajo": "000000aa",
            "c_inactivo": "000000aa",
            "redondeado": 0,
            "terminal": "terminology",
            "fileManager": "nautilus",
            "menu": "wofi --show drun"
        }
        self.state = self.load_state()
        
        # Variables de Tkinter
        self.t_borde = tk.IntVar(value=self.state["t_borde"])
        self.c_arriba = tk.StringVar(value=self.state["c_arriba"])
        self.c_abajo = tk.StringVar(value=self.state["c_abajo"])
        self.c_inactivo = tk.StringVar(value=self.state["c_inactivo"])
        self.redondeado = tk.IntVar(value=self.state["redondeado"])
        self.terminal = tk.StringVar(value=self.state["terminal"])
        self.fileManager = tk.StringVar(value=self.state["fileManager"])
        self.menu = tk.StringVar(value=self.state["menu"])
        
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

        tk.Label(self.root, text="Terminal:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.terminal, width=20).grid(row=5, column=1, columnspan=2, padx=5)

        tk.Label(self.root, text="File Manager:").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.fileManager, width=20).grid(row=6, column=1, columnspan=2, padx=5)

        tk.Label(self.root, text="Menu:").grid(row=7, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.menu, width=20).grid(row=7, column=1, columnspan=2, padx=5)

        tk.Button(self.root, text="Guardar configuración", command=self.save_config).grid(row=8, column=0, columnspan=3, pady=10)

        tk.Button(self.root, text="Atajos de teclado", command=self.show_shortcuts).grid(row=9, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Nuevo atajo", command=self.new_shortcut_window).grid(row=10, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Editar manualmente", command=self.edit_config).grid(row=11, column=0, columnspan=3, pady=10)

    def pick_color(self, color_var):
        initial_color = f"#{color_var.get()[:6]}"
        color_code = colorchooser.askcolor(color=initial_color, title="Selecciona un color")[1]
        if color_code:
            color_var.set(color_code[1:] + "aa")  # Convertir a formato hex con "aa" final

    def save_config(self):
        if not self.config_path.exists():
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
            lines[5] = f"$terminal = {self.terminal.get()}\n"
            lines[6] = f"$fileManager = {self.fileManager.get()}\n"
            lines[7] = f"$menu = {self.menu.get()}\n"

            with open(self.config_path, "w") as file:
                file.writelines(lines)

            messagebox.showinfo("Éxito", "Configuración guardada exitosamente.")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la configuración: {e}")

    def load_state(self):
        state = self.default_state.copy()
        if self.config_path.exists():
            try:
                with open(self.config_path, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.startswith("$t_borde"):
                            state["t_borde"] = int(line.split("=")[1].strip())
                        elif line.startswith("$c_arriba"):
                            state["c_arriba"] = line.split("=")[1].strip()
                        elif line.startswith("$c_abajo"):
                            state["c_abajo"] = line.split("=")[1].strip()
                        elif line.startswith("$c_inactivo"):
                            state["c_inactivo"] = line.split("=")[1].strip()
                        elif line.startswith("$redondeado"):
                            state["redondeado"] = int(line.split("=")[1].strip())
                        elif line.startswith("$terminal"):
                            state["terminal"] = line.split("=")[1].strip()
                        elif line.startswith("$fileManager"):
                            state["fileManager"] = line.split("=")[1].strip()
                        elif line.startswith("$menu"):
                            state["menu"] = line.split("=")[1].strip()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el estado: {e}")
        return state

    @staticmethod
    def validate_color(color):
        return len(color) == 8 and all(c in "0123456789abcdefABCDEF" for c in color)

    def show_shortcuts(self):
        shortcuts_window = tk.Toplevel(self.root)
        shortcuts_window.title("Atajos de teclado")

        frame = tk.Frame(shortcuts_window)
        frame.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame)
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.shortcuts = self.load_shortcuts()
        self.shortcut_entries = []

        for i, (keys, command) in enumerate(self.shortcuts):
            tk.Label(scrollable_frame, text=keys).grid(row=i, column=0, padx=10, pady=5)
            command_entry = tk.Entry(scrollable_frame, width=50)
            command_entry.insert(0, command)
            command_entry.grid(row=i, column=1, padx=10, pady=5)
            self.shortcut_entries.append(command_entry)
            tk.Button(scrollable_frame, text="Borrar", command=lambda i=i: self.comment_shortcut(i)).grid(row=i, column=2, padx=10, pady=5)

        tk.Button(scrollable_frame, text="Guardar cambios", command=lambda: self.save_shortcuts()).grid(row=len(self.shortcuts), column=0, columnspan=3, pady=10)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_shortcuts(self):
        shortcuts = []
        with open(self.config_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("bind ="):
                    parts = line.split(",")
                    keys = parts[0].split("=")[1].strip()
                    if keys == "":
                        keys = parts[1].strip()
                        command = ",".join(parts[2:]).strip()
                    else:
                        keys = parts[0].split("=")[1].strip() + " + " + parts[1].strip()
                        command = ",".join(parts[2:]).strip()
                    shortcuts.append((keys, command))
        return shortcuts

    def save_shortcuts(self):
        with open(self.config_path, "r") as file:
            lines = file.readlines()

        bind_lines = [i for i, line in enumerate(lines) if line.startswith("bind =")]

        for i, entry in enumerate(self.shortcut_entries):
            if entry.cget("state") != tk.DISABLED:
                command = entry.get()
                keys = self.shortcuts[i][0]
                if " + " in keys:
                    key_parts = keys.split(" + ")
                    lines[bind_lines[i]] = f"bind = {key_parts[0]}, {key_parts[1]}, {command}\n"
                else:
                    lines[bind_lines[i]] = f"bind = , {keys}, {command}\n"

        with open(self.config_path, "w") as file:
            file.writelines(lines)

        messagebox.showinfo("Éxito", "Atajos de teclado guardados exitosamente.")

    def comment_shortcut(self, row):
        with open(self.config_path, "r") as file:
            lines = file.readlines()

        bind_lines = [i for i, line in enumerate(lines) if line.startswith("bind =")]

        if row < len(bind_lines):
            lines[bind_lines[row]] = f"# {lines[bind_lines[row]]}"

        with open(self.config_path, "w") as file:
            file.writelines(lines)

        self.shortcut_entries[row].config(state=tk.DISABLED, disabledbackground="red", disabledforeground="white")
        messagebox.showinfo("Éxito", "Atajo de teclado borrado exitosamente.")

    def new_shortcut_window(self):
        new_shortcut_window = tk.Toplevel(self.root)
        new_shortcut_window.title("Nuevo atajo")

        tk.Label(new_shortcut_window, text="Teclas:").grid(row=0, column=0, padx=10, pady=5)
        self.keys_var = tk.StringVar()
        keys_entry = tk.Entry(new_shortcut_window, textvariable=self.keys_var, width=20, state='readonly')
        keys_entry.grid(row=0, column=1, padx=10, pady=5)
        keys_entry.bind("<KeyPress>", self.detect_keys)

        tk.Button(new_shortcut_window, text="Borrar", command=lambda: self.keys_var.set("")).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(new_shortcut_window, text="Comando:").grid(row=1, column=0, padx=10, pady=5)
        self.command_var = tk.StringVar()
        command_entry = tk.Entry(new_shortcut_window, textvariable=self.command_var, width=50)
        command_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(new_shortcut_window, text="Aceptar", command=lambda: self.add_shortcut(new_shortcut_window)).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(new_shortcut_window, text="Cancelar", command=new_shortcut_window.destroy).grid(row=2, column=1, padx=10, pady=10)

    def detect_keys(self, event):
        key = event.keysym
        if key == "Super_L":
            key = "$mainMod"
        if self.keys_var.get():
            self.keys_var.set(self.keys_var.get() + " + " + key)
        else:
            self.keys_var.set(key)

    def add_shortcut(self, window):
        keys = self.keys_var.get()
        command = self.command_var.get()
        if not keys or not command:
            messagebox.showerror("Error", "Debe ingresar las teclas y el comando.")
            return

        new_bind = f"bind = {keys.replace(' + ', ', ')}, exec, {command}\n"

        with open(self.config_path, "r") as file:
            lines = file.readlines()

        last_bind_index = max(i for i, line in enumerate(lines) if line.startswith("bind ="))
        lines.insert(last_bind_index + 1, new_bind)

        with open(self.config_path, "w") as file:
            file.writelines(lines)

        messagebox.showinfo("Éxito", "Nuevo atajo agregado exitosamente.")
        window.destroy()

    def edit_config(self):
        os.system("code ~/.config/hypr/hyprland.conf")


# Crear ventana de la aplicación
root = tk.Tk()
app = ConfigEditor(root)
root.mainloop()