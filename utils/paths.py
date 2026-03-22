# -----------------------------------------------------------------------------------------------------------------------------------------

# DOCUMENTACIÓN:

""" Utilidades de Rutas para el Juego de Memoria """

# NOTE: Fecha de Realización: 15/10/2025
# NOTE: Autor: Magallanes López Carlos Gabriel
# NOTE: Correo: cgmagallanes23@gmail.com

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Módulos Importados ============================================================= """

# Dependencias 
from pathlib import Path                                                      # Módulo para Manipulación de Rutas de Archivos y Directorios

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Ruta Base ============================================================= """

# Ruta Base del Proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------------------------------------------------------------------
""" ======================================================== Carga de Imágenes ============================================================= """

# Función: Obtener la Ruta Completa de una Imagen
def get_image_path(image_name: str) -> str:
    
    """
       -  Función: Obtener la Ruta Completa de una Imagen
       -  Argumentos:
            - image_name (str): Nombre del Archivo de la Imagen
       -  Retorno: Ruta Completa de la Imagen (str)
       -  Objetivo: Construir la Ruta Completa de una Imagen en el Proyecto
    """

    # Construye y Retorna la Ruta Completa de la Imagen
    return str(BASE_DIR / "imgs" / image_name)  




# Función: Obtener la Ruta Completa de Música
def get_music_path(filename: str) -> str:
    
    """
       - Función: Obtener Ruta de Música
       - Argumentos: 
            - filename (str) - Nombre del Archivo de Música
       - Retorno: Ruta Completa del Música (str)
       - Objetivo: Construir la Ruta Completa de un Archivo de Música
    """

    # Construye y Retorna la Ruta Completa de la Musica
    return str(BASE_DIR / "music" / filename)

# -----------------------------------------------------------------------------------------------------------------------------------------