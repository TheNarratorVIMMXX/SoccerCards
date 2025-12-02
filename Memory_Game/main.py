# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Memorama de Fútbol """

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Ocultar el Mensaje de Bienvenida de Pygame
import os                                           # Módulo para interactuar con el Sistema Operativo
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"      # Variable para ocultar el Mensaje de Bienvenida de Pygame

import pygame                                      # Módulo para Desarrollo de videojuegos
import sys                                         # Módulo para interactuar con el Intérprete de Python
import random                                      # Módulo para generar Números Aleatorios
import math                                        # Módulo para Funciones Matemáticas
import time                                        # Módulo para Funciones relacionadas con el Tiempo

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Inicialización Pygame ============================================================= """

# Inicialización de Pygame
pygame.init()

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Constantes del Juego ============================================================= """

# Constantes de Configuración de la Pantalla
CARD_SIZE = 200                                     # Tamaño de cada Tarjeta (Ancho y Alto)
SCREEN_WIDTH = CARD_SIZE * 4                        # Ancho de la Pantalla (4 Tarjetas por Fila)
BUTTON_HEIGHT = 50                                  # Alto del Botón de Inicio
SCREEN_HEIGHT = (CARD_SIZE * 2) + BUTTON_HEIGHT     # Alto de la Pantalla (2 Filas de Tarjetas + Botón)
BUTTON_WIDTH = SCREEN_WIDTH                         # Ancho del Botón igual al de la Pantalla

# Constantes de Fuente para el Texto del Botón
FONT_SIZE = 20                                           # Tamaño de la Fuente del Texto del Botón
FONT = pygame.font.SysFont("Arial", FONT_SIZE)           # Fuente del Texto del Botón
X_FONT = int((BUTTON_WIDTH / 2) - (FONT_SIZE / 2)) - 45  # Posición X del Texto del Botón 
Y_FONT = int(SCREEN_HEIGHT - BUTTON_HEIGHT) + 12         # Posición Y del Texto del Botón

# Constantes de Colores (RGB)
WHITE = (255, 255, 255)                             # Color Blanco
BLACK = (0, 0, 0)                                   # Color Negro
GRAY = (206, 206, 206)                              # Color Gris
GREEN = (0, 255, 0)                                 # Color Verde

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Clase Tarjeta ============================================================= """

# Clase: Tarjeta
class Card:
    
    """
        - Clase: Tarjeta
        - Atributos:
            - show (bool): Indica si la Tarjeta está boca arriba
            - discovered (bool): Indica si la Tarjeta ha sido emparejada
            - image_path (str): Ruta de la Imagen de la Tarjeta
            - real_image (Surface): Imagen cargada de la Tarjeta
        - Métodos:
            - __init__(self, image_path): Inicializa una Tarjeta con la Imagen dada
        - Objetivo: Representar una Tarjeta del Juego de Memoria
    """

    # Método: Inicializador de la Clase
    def __init__(self, image_path: str) -> None:
        
        """
           -  Método: Inicializador de la Clase
           -  Argumentos:
                - image_path (str): Ruta de la Imagen de la Tarjeta
           -  Retorno: Ninguno
           -  Objetivo Principal: Inicialización de los Atributos de la Clase
        """
        
        # Validación del Argumento: Ruta de Imagen
        if not isinstance(image_path, str): raise TypeError("La Ruta de la Imagen debe ser una Cadena de Texto (str).")
        elif not image_path.strip(): raise ValueError("La Ruta de la Imagen no puede estar Vacía.")

        # Atributos de la Clase
        self.show: bool = True                                             # Indica si la Tarjeta está boca arriba
        self.discovered: bool = False                                      # Indica si la Tarjeta ha sido emparejada
        self.image_path: str = image_path                                  # Ruta de la Imagen de la Tarjeta
        self.real_image: pygame.Surface = pygame.image.load(image_path)    # Imagen cargada de la Tarjeta

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Configuración ============================================================= """

# Configuración de la Pantalla
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))            # Crear la Ventana del Juego
pygame.display.set_caption("Memory Game - Fútbol Edition")                      # Título de la Ventana


# Variables para el Estado del Juego
game_started = False                            # Indica si el Juego ha comenzado
can_play = True                                 # Indica si el Jugador puede interactuar
x1, y1, x2, y2 = None, None, None, None         # Coordenadas de las Tarjetas seleccionadas
show_card_time = 1                              # Segundos para mostrar Tarjetas no emparejadas
final_seconds = None                         # Marca de Tiempo para ocultar Tarjetas


# Configuración de las Tarjetas del Juego
cards = [
    
    [Card("imgs/PSG.png"), Card("imgs/Madrid.png"), Card("imgs/Barca.png"), Card("imgs/Inter.png")],
    [Card("imgs/PSG.png"), Card("imgs/Madrid.png"), Card("imgs/Barca.png"), Card("imgs/Inter.png")]    

]


# Configuración del Botón de Inici
boton = pygame.Rect(0, SCREEN_HEIGHT - BUTTON_HEIGHT, BUTTON_WIDTH, SCREEN_HEIGHT)

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Helpers ============================================================= """

# Función: Ocultar Todas las Tarjetas
def hide_all_cards() -> None:
    
    """
       -  Función: Ocultar Todas las Tarjetas
       -  Argumentos: Ninguno
       -  Retorno: Ninguno
       -  Objetivo Principal: Ocultar todas las Tarjetas en la Cuadrícula
    """
    
    # Oculta todas las Tarjetas en la Cuadrícula
    for row in cards:                             # Itera sobre cada Fila de Tarjetas
        for card in row:                          # Itera sobre cada Tarjeta en la Fila
            card.show = False                     # Oculta la Tarjeta
            card.discovered = False               # Marca la Tarjeta como no emparejada




# Función: Aleatorizar las Tarjetas
def randomize_cards() -> None:
    
    """
       -  Función: Aleatorizar las Tarjetas
       -  Argumentos: Ninguno
       -  Retorno: Ninguno
       -  Objetivo Principal: Aleatorizar las Tarjetas en la Cuadrícula
    """
    
    # Obtención de las Dimensiones de la Cuadrícula
    rows = len(cards)                                # Número de Filas
    columns = len(cards[0])                          # Número de Columnas
    
    # Aleatorización de las Tarjetas
    for y in range(rows):                                 # Itera sobre cada Fila
        for x in range(columns):                          # Itera sobre cada Columna
            random_x = random.randint(0, columns - 1)     # Índice Aleatorio de Columna
            random_y = random.randint(0, rows - 1)        # Índice Aleatorio de Fila
            temp_card = cards[y][x]                       # Tarjeta Temporal
            cards[y][x] = cards[random_y][random_x]       # Intercambia Tarjetas
            cards[random_y][random_x] = temp_card         # Completa el Intercambio




# Función: Comprobar si el Jugador ha Ganado
def is_a_win() -> None:
    
    """
       -  Función: Comprobar si el Jugador ha Ganado
       -  Argumentos: Ninguno
       -  Retorno: Ninguno
       -  Objetivo Principal: Comprobar si el Jugador ha Ganado
    """

    # Si el Jugador ha Ganado, reinicia el Juego
    if win(): restart_game()




# Función: Ganar el Juego
def win() -> bool:

    """
       -  Función: Ganar el Juego
       -  Argumentos: Ninguno
       -  Retorno: Ninguno
       -  Objetivo Principal: Verificar si todas las Tarjetas han sido Descubiertas
    """

    # Verifica si todas las Tarjetas han sido Descubiertas
    for row in cards:                                        # Itera sobre cada Fila de Tarjetas
        for card in row:                                     # Itera sobre cada Tarjeta en la Fila
            if not card.discovered: return False             # Si alguna Tarjeta no está Descubierta, retorna False
    return True                                              # Si todas las Tarjetas están Descubiertas, retorna True




# Función: Reiniciar el Juego
def restart_game() -> None:
    
    """
       -  Función: Reiniciador del Juego
       -  Argumentos: Ninguno
       -  Retorno: Ninguno
       -  Objetivo Principal: Inicialización de los Atributos de la Clase
    """

    # Reinicia el Juego
    global game_started                      # Declara la Variable Global
    game_started = False                     # Reinicia el Estado del Juego




# Función: Iniciar el Juego
def start_game() -> None:
    """
       -  Función: Iniciar el Juego
       -  Argumentos: Ninguno
       -  Retorno: Ninguno
       -  Objetivo Principal: Preparar el Tablero del Juego
    """

    # Inicia el Juego
    global game_started                      # Declara la Variable Global
    for _ in range(1, 4): randomize_cards()  # Aleatoriza las Tarjetas varias veces
    hide_all_cards()                         # Oculta todas las Tarjetas
    game_started = True                      # Cambia el Estado del Juego a Iniciado

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Game Loop ============================================================= """

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Bucle Principal del Juego
while True:

    # Gestión del Temporizador para ocultar Tarjetas no Emparejadas
    if ((not can_play and final_seconds is not None) and              # Si no se puede jugar y el Temporizador está activo
        (int(time.time()) - final_seconds >= show_card_time)):        # Y ha pasado el tiempo para mostrar las Tarjetas
            cards[y1][x1].show = False                                # Oculta la primera Tarjeta seleccionada
            cards[y2][x2].show = False                                # Oculta la segunda Tarjeta seleccionada
            x1, y1, x2, y2 = None, None, None, None                   # Resetea las coordenadas de las Tarjetas seleccionadas
            can_play = True                                           # Permite jugar de nuevo
            final_seconds = None                                      # Resetea el Temporizador

    # Renderizado del Fondo
    game_screen.fill(WHITE)

    # Renderizado de las Tarjetas
    for row_index, row in enumerate(cards):                                                                                # Itera sobre cada Fila de Tarjetas
        for card_index, card in enumerate(row):                                                                            # Itera sobre cada Tarjeta en la Fila
            if card.show or card.discovered:                                                                               # Si la Tarjeta está boca arriba o ha sido emparejada
                game_screen.blit(card.real_image, (card_index * CARD_SIZE, row_index * CARD_SIZE))                         # Dibuja la Imagen de la Tarjeta
            else:                                                                                                          # Si la Tarjeta está boca abajo
                pygame.draw.rect(game_screen, GRAY, (card_index * CARD_SIZE, row_index * CARD_SIZE,CARD_SIZE, CARD_SIZE))  # Dibuja el Reverso de la Tarjeta
            pygame.draw.rect(game_screen, BLACK, (card_index * CARD_SIZE, row_index * CARD_SIZE, CARD_SIZE, CARD_SIZE), 2) # Dibuja el Borde de la Tarjeta

    # Renderizado del botón de inicio
    pygame.draw.rect(game_screen, WHITE if game_started else GREEN, boton)                                                 # Dibuja el Botón
    game_screen.blit(FONT.render("Iniciar juego", True, GRAY if game_started else WHITE), (X_FONT, Y_FONT))                # Dibuja el Texto del Botón

    # Gestión de Eventos de Entrada
    for event in pygame.event.get():                                         # Itera sobre cada Evento en la Cola de Eventos
        if event.type == pygame.QUIT:                                        # Si el Evento es de Salida
            pygame.quit()                                                    # Cierra Pygame               
            sys.exit()                                                       # Sale del Programa
        elif event.type == pygame.MOUSEBUTTONDOWN and can_play:              # Si el Evento es un Clic del Mouse y se puede jugar
            absolute_x, absolute_y = event.pos                               # Obtiene las Coordenadas Absolutas del Clic            
            if boton.collidepoint(event.pos):                                # Si el Clic está dentro del Botón
                if not game_started: start_game()                            # Inicia el Juego si no ha comenzado
                continue                                                     # Continúa al siguiente Evento
            if not game_started: continue                                    # Si el Juego no ha comenzado, ignora el Clic

            # Cálculo de las Coordenadas de la Tarjeta en la Cuadrícula
            x = math.floor(absolute_x / CARD_SIZE)                           # Coordenada X de la Tarjeta
            y = math.floor(absolute_y / CARD_SIZE)                           # Coordenada Y de la Tarjeta
            
            # Validación de Límites de la Cuadrícula
            if y >= len(cards) or x >= len(cards[0]): continue

            # Obtención de la Tarjeta Seleccionada
            card = cards[y][x]                                              # Tarjeta en la Posición (x, y)
            if card.show or card.discovered: continue                       # Si la Tarjeta ya está boca arriba o emparejada, ignora el Clic

            # Lógica de Selección de Tarjetas
            if x1 is None and y1 is None:                                  # Primera tarjeta seleccionada
                x1, y1 = x, y                                              # Guarda las Coordenadas de la Primera Tarjeta
                cards[y1][x1].show = True                                  # Muestra la Primera Tarjeta
            else:                                                          # Segunda tarjeta seleccionada
                x2, y2 = x, y                                              # Guarda las Coordenadas de la Segunda Tarjeta
                cards[y2][x2].show = True                                  # Muestra la Segunda Tarjeta
                card1 = cards[y1][x1]                                      # Primera Tarjeta Seleccionada
                card2 = cards[y2][x2]                                      # Segunda Tarjeta Seleccionada
                
                # Verificación de Coincidencia
                if card1.image_path == card2.image_path:                   # Si las Tarjetas coinciden
                    cards[y1][x1].discovered = True                        # Marca la Primera Tarjeta como Descubierta
                    cards[y2][x2].discovered = True                        # Marca la Segunda Tarjeta como Descubierta
                    x1, y1, x2, y2 = None, None, None, None                # Resetea las Coordenadas de las Tarjetas Seleccionadas
                else:                                                      # Si las Tarjetas no coinciden
                    final_seconds = int(time.time())                       # Inicia el Temporizador para ocultar las Tarjetas
                    can_play = False                                       # Bloquea la Interacción hasta ocultar las Tarjetas
            
            # Verificación de Victoria
            is_a_win()

    # Actualización de la Pantalla
    pygame.display.flip()                      # Actualiza la Pantalla
    clock.tick(60)                             # Limita a 60 FPS

    # -----------------------------------------------------------------------------------------------------------------------------------------