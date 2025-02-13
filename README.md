# Hyprland interface configuration and editor

Este proyecto contiene mi archivo personal de configuración de hyprland (Arch Linux) junto a un pequeño programa .py para editar los bordes de la panatalla.

## Archivos Importantes

### `hyprland.conf`
El archivo `hyprland.conf` es crucial para ajustar las ventanas en Arch Linux. Dentro de este archivo, puedes configurar diversas opciones que te permiten personalizar el comportamiento y la apariencia de las ventanas.

#### Normas Concretas para Ventanas:
- **Reglas de tamaño y posición**: Define el tamaño y la posición inicial de las ventanas.
- **Comportamiento de las ventanas**: Configura cómo las ventanas deben comportarse en diferentes escenarios (maximizar, minimizar, etc.).

#### Atajos para el Teclado:
Configura atajos de teclado para mejorar la eficiencia y la productividad. Aquí tienes algunos ejemplos:
- **Meta + Q** = Consola
- **Meta + C** = Cerrar Ventana
- **Meta + E** = Buscador
- **Meta + R** = Aplicaciones
- **Meta + T** = Sistema
- **Meta + Y** = Estilos
- **Meta + Z** = Archivos
- **Meta + F** = Firefox
- **Meta + X** = Modo Flotante
- **Meta + J** = Ajustar Horizontal/Vertical
- **Meta + O** = Abrir Marcadores
- **Meta + K** = Cerrar Marcadores
- **Meta + num** = Cambiar Escritorios
- **Meta + S** = Ventana Secreta
- **Meta + Shift + []** = Mover Ventanas
- **Meta + I** = Cambiar Color Hypr
- **Meta + A** = Crear Agrupación
- **Meta + D** = Desagrupar
- **Meta + G** = Agrandar Ventana
- **Meta + TAB** = Cambiar Escritorios
- **Meta + H** = Ajustar Horizontal
- **Meta + V** = Ajustar Vertical
- **Meta + F1-F3** = Abrir Stickers
- **Meta + F4** = Cerrar Stickers
- **Meta + F5-F6** = Controlar Sonidos
- **Meta + F9** = Reducir Brillo
- **Meta + F10** = Aumentar Brillo
- **Meta + F12** = Brillo 0
- **Meta + Audio** = Todas las opciones de Audio

Además, puedes instalar extensiones de Hyprland desde `hyprpm` para ampliar las funcionalidades y mejorar aún más la personalización.

![2025-01-19-165504_hyprshot](https://github.com/user-attachments/assets/a2386da4-82ff-4c9c-b45c-408887518a96)


### `interfaz.py`
El archivo `interfaz.py` se encarga de ajustar el tamaño, color y degradado del borde de las ventanas de Hyprland, proporcionando una interfaz más atractiva y coherente.

#### Funcionalidades del Script:
- **Ajuste de tamaño**: Permite cambiar el tamaño de los bordes de las ventanas.
- **Ajuste de color**: Cambia los colores de los bordes para adaptarse a diferentes temas y estilos.
- **Degradado**: Añade degradados a los bordes para un look más moderno y sofisticado.

Este script utiliza un archivo `.json` para guardar el estado anterior de la configuración, asegurando que no se pierdan los ajustes tras un reinicio.

#### Archivos Relacionados:
- **`hyprland_editor_state.json`**: Este archivo guarda el estado anterior de la configuración para mantener los ajustes al reiniciar. De esta manera, cualquier cambio que realices se conservará la próxima vez que inicies tu sistema.

![2025-01-19-165612_hyprshot](https://github.com/user-attachments/assets/64651eb3-4fca-4bcf-8089-8ddfc3d9b6d4)


### Instalación y Uso
Para utilizar estos archivos en tu sistema, sigue estos pasos:

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/garcilaso05/myhyprlandconf.git
    ```

2. **Copia los archivos a tu directorio de configuración**:
    ```bash
    cp hyprland.conf ~/.config/hypr/
    cp interfaz.py ~/.config/hypr/
    ```

3. **Asegúrate de que los scripts tengan permisos de ejecución**:
    ```bash
    chmod +x ~/.config/hypr/interfaz.py
    ```

### Usar solo el gestor de interfaz:
Copia todos las referencias de las variables globales en tu `hyprland.conf`.

```bash
$t_borde = 4
$c_arriba = 00b9d9aa
$c_abajo = ffd40eaa
$c_inactivo = 001949aa
$redondeado = 2
```

```bash

general {
    # See https://wiki.hyprland.org/Configuring/Variables/ for more

    gaps_in = 5
    gaps_out = 20
    border_size = $t_borde
    col.active_border = rgba($c_arriba) rgba($c_abajo) 45deg
    col.inactive_border = rgba($c_inactivo)

    layout = hy3
    #     layout = dwindle

    # Please see https://wiki.hyprland.org/Configuring/Tearing/ before you turn this on
    allow_tearing = false
}

decoration {
    # See https://wiki.hyprland.org/Configuring/Variables/ for more

    rounding = $redondeado
    
    blur {
        enabled = true
        size = 5
        passes = 1
    }

#    drop_shadow = yes
#    shadow_range = 4
#    shadow_render_power = 3
#    col.shadow = rgba(1a1a1aee)
}
```
<sup><sup style="color: grey;">by Roger García Doncel</sup></sup>
