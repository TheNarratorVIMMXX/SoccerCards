# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Clase Tarjeta para el Juego de Memoria """

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias
import pygame                                                                               # Módulo para Desarrollo de videojuegos

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
        if not isinstance(image_path, str): 
            raise TypeError("La Ruta de la Imagen debe ser una Cadena de Texto (str).")
        elif not image_path.strip(): 
            raise ValueError("La Ruta de la Imagen no puede estar Vacía.")

        # Atributos de la Clase
        self.show: bool = True                                                              # Indica si la Tarjeta está boca arriba
        self.discovered: bool = False                                                       # Indica si la Tarjeta ha sido emparejada
        self.image_path: str = image_path                                                   # Ruta de la Imagen de la Tarjeta
        self.real_image: pygame.Surface = pygame.image.load(image_path)                     # Imagen cargada de la Tarjeta

# -----------------------------------------------------------------------------------------------------------------------------------------