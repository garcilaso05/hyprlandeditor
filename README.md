# Hyprland Config Editor

Este proyecto proporciona una interfaz gráfica para editar la configuración de Hyprland. Permite modificar los bordes de las ventanas, los colores, los atajos de teclado y más.

![2025-02-20-141045_hyprshot](https://github.com/user-attachments/assets/2dfe0741-eec0-4811-a539-492dc7a375d9)


## Funcionalidades

### Configuración de Bordes y Colores

- **Tamaño del borde**: Permite ajustar el tamaño del borde de las ventanas.
- **Color arriba**: Permite seleccionar el color de la parte superior del borde.
- **Color abajo**: Permite seleccionar el color de la parte inferior del borde.
- **Color inactivo**: Permite seleccionar el color del borde cuando la ventana está inactiva.
- **Redondeado**: Permite ajustar el nivel de redondeo de las esquinas de las ventanas.

### Programas Principales

- **Terminal**: Permite definir el terminal predeterminado.
- **File Manager**: Permite definir el gestor de archivos predeterminado.
- **Menu**: Permite definir el menú de aplicaciones predeterminado.

### Atajos de Teclado

- **Mostrar Atajos de Teclado**: Muestra una ventana con todos los atajos de teclado configurados. Permite editar y borrar atajos existentes.
- **Nuevo Atajo**: Abre una ventana para crear un nuevo atajo de teclado. Permite detectar combinaciones de teclas y asignar un comando.
- **Guardar Cambios**: Guarda los cambios realizados en los atajos de teclado.
- **Borrar Atajo**: Permite comentar un atajo de teclado para desactivarlo.

### Edición Manual

- **Editar Manualmente**: Abre el archivo de configuración `hyprland.conf` en el editor de código para realizar ediciones manuales.

## Uso

1. Clona este repositorio:
    ```sh
    git clone https://github.com/blackhole/hyprlandeditor.git
    cd hyprlandeditor
    ```

2. Ejecuta el script `interfaz.py` desde cualquier carpeta:
    ```sh
    python3 /path/to/hyprlandeditor/interfaz.py
    ```

## Requisitos

- Python 3
- Tkinter

## Notas

- El archivo de configuración `hyprland.conf` debe estar ubicado en `~/.config/hypr/hyprland.conf`.
- El script `interfaz.py` puede ejecutarse desde cualquier carpeta.
