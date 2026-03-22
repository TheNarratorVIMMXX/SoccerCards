# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Constantes del Memorama de Fútbol """

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias
import pygame                                                        # Módulo para Desarrollo de videojuegos

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Constantes del Juego ============================================================= """

# Constantes de Configuración de la Pantalla
CARD_SIZE = 200                                                      # Tamaño de cada Tarjeta (Ancho y Alto)
SCREEN_WIDTH = CARD_SIZE * 4                                         # Ancho de la Pantalla (4 Tarjetas por Fila)
BUTTON_HEIGHT = 50                                                   # Alto del Botón de Inicio
SCREEN_HEIGHT = (CARD_SIZE * 2) + BUTTON_HEIGHT                      # Alto de la Pantalla (2 Filas de Tarjetas + Botón)
BUTTON_WIDTH = SCREEN_WIDTH                                          # Ancho del Botón igual al de la Pantalla

# Constantes de Fuente para el Texto del Botón
FONT_SIZE = 20                                                       # Tamaño de la Fuente del Texto del Botón
FONT = pygame.font.SysFont("Arial", FONT_SIZE)                       # Fuente del Texto del Botón
X_FONT = int((BUTTON_WIDTH / 2) - (FONT_SIZE / 2)) - 45              # Posición X del Texto del Botón 
Y_FONT = int(SCREEN_HEIGHT - BUTTON_HEIGHT) + 12                     # Posición Y del Texto del Botón

# -----------------------------------------------------------------------------------------------------------------------------------------