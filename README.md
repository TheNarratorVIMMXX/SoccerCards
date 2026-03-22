# 🃏 Juego de Memoria - Edición Fútbol

Un **Juego de Memoria con Cartas** completamente funcional con temática de fútbol, desarrollado con **Pygame**. Este proyecto demuestra conceptos de programación de videojuegos, incluyendo diseños en cuadrícula, manejo de eventos, gestión de estados y mecánicas de juego interactivas.

---

## 👨‍🎓 Información del Desarrollador

- **Autor:** Magallanes López Carlos Gabriel
- **Correo:** cgmagallanes23@gmail.com
- **Fecha de Desarrollo:** 15 de octubre de 2025

---

## 🎮 Descripción del Juego

Este es un clásico juego de memorama con logos de equipos de fútbol. Los jugadores deben encontrar pares de cartas iguales voltéandolas de dos en dos. El juego incluye:

- **Diseño en cuadrícula** con 8 cartas (4 pares) organizadas en una cuadrícula de 2x4
- **Mecánica de volteo de cartas** con animaciones de revelación fluidas
- **Sistema de detección de pares** para cartas emparejadas
- **Funcionalidad de ocultamiento automático** para pares que no coinciden
- **Detección de victoria** cuando se encuentran todos los pares
- **Aleatorización** de posiciones de cartas para mayor rejugabilidad
- **Botón de inicio interactivo** para comenzar nuevas partidas

---

## 🎯 Mecánicas de Juego

### Controles
- **Clic del Mouse**: Seleccionar y voltear cartas
- **Botón de Inicio**: Comenzar una nueva partida con cartas mezcladas

### Objetivo
Encontrar los 4 pares de cartas de equipos de fútbol recordando sus posiciones. Las cartas se voltean de regreso si no coinciden.

### Reglas del Juego
1. Haz clic en el botón "Iniciar juego" para comenzar
2. Haz clic en cualquier carta para revelarla
3. Haz clic en una segunda carta para intentar encontrar un par
4. Si las cartas coinciden, permanecen reveladas
5. Si las cartas no coinciden, se voltean después de 1 segundo
6. Continúa hasta encontrar todos los pares
7. El juego se reinicia automáticamente cuando ganas

---

## 🚀 Características

### ✨ Características Principales de Juego
- **Sistema de Cuadrícula de Cartas**: Diseño en cuadrícula 2x4 con 4 logos únicos de equipos de fútbol
- **Detección de Pares**: Comparación automática de cartas seleccionadas
- **Revelación Temporizada**: Las cartas sin par se ocultan después de 1 segundo
- **Condición de Victoria**: Detección automática de victoria y reinicio del juego
- **Mezcla de Cartas**: Posiciones aleatorias al inicio del juego
- **Gestión de Estados**: Seguimiento de cartas descubiertas y mostradas

### 🎨 Elementos Visuales
- **Logos de Equipos de Fútbol**: PSG, Real Madrid, Barcelona e Inter de Milán
- **Diseño del Reverso de las Cartas**: Diseño gris limpio para cartas ocultas
- **Resaltado de Bordes**: Bordes negros alrededor de cada carta
- **Botón de Inicio**: Botón verde que se vuelve blanco durante el juego
- **Renderizado Fluido**: Juego a 60 FPS

### 🎮 Elementos Interactivos
- **Detección de Clics**: Seguimiento preciso de la posición del mouse
- **Estados del Botón**: Retroalimentación visual para el botón de inicio
- **Estados de las Cartas**: Tres estados (oculta, mostrada, descubierta)
- **Bloqueo de Turno**: Evita clics durante la comparación de cartas

---

## 📦 Requisitos

### Descarga
El juego está disponible como ejecutable, **no requiere instalar Python ni ninguna dependencia adicional**.

> 📥 Descarga el archivo `.exe` desde la sección de [Releases](https://github.com/TheNarratorVIMMXX/SoccerCards/releases) y ejecútalo directamente.

---

### 🖥️ Requisitos del Sistema
- **SO:** Windows 7/8/10/11
- **RAM:** 2GB
- **Almacenamiento**: ~50 MB de espacio libre

---

## 🎮 Cómo Ejecutar

1. **Descarga el ejecutable** desde la sección de [Releases](https://github.com/TheNarratorVIMMXX/SoccerCards/releases)
2. **Haz doble clic** en el archivo `.exe`
3. **¡Listo!** El juego abrirá directamente, sin instalaciones ni configuraciones adicionales

---

## 🔧 Implementación Técnica

### Arquitectura del Juego

```python
# Componentes Principales:
1. Clase Carta (Diseño orientado a objetos)
2. Configuración de Pantalla (Ventana Pygame)
3. Sistema de Diseño en Cuadrícula (Arreglo 2D)
4. Ciclo de Manejo de Eventos
5. Gestión de Estados
```

## 🎨 Diseño Visual

### Paleta de Colores
- **Fondo**: Blanco (`#FFFFFF`)
- **Reverso de Carta**: Gris (`#CECECE`)
- **Borde de Carta**: Negro (`#000000`)
- **Botón de Inicio (Activo)**: Verde (`#00FF00`)
- **Botón de Inicio (Jugando)**: Blanco (`#FFFFFF`)
- **Texto del Botón**: Dinámico (Blanco/Gris según el estado)

### Estados de las Cartas
1. **Oculta**: Rectángulo gris con borde negro
2. **Mostrada**: Logo del equipo visible
3. **Descubierta**: Logo del equipo permanentemente visible

---

## 🐛 Limitaciones Conocidas

- Tamaño de ventana fijo de 800x450 (no redimensionable)
- Solo 4 pares de cartas (8 en total)
- Sin sistema de puntuación ni temporizador
- Sin niveles de dificultad

---

## 📚 Resultados de Aprendizaje

Este proyecto sirve como recurso educativo para comprender conceptos fundamentales del desarrollo de videojuegos:

### 🎓 Lo que Aprenderás

1. **Programación Orientada a Objetos**
   - Diseño y encapsulamiento de clases
   - Atributos y métodos de instancia
   - Gestión del estado de objetos
   - Sugerencias de tipo y validación

2. **Fundamentos de Pygame**
   - Configuración de ventana y pantalla
   - Arquitectura del ciclo de eventos
   - Manejo de entrada del mouse
   - Renderizado de superficies e imágenes
   - Detección de colisiones con rectángulos

3. **Lógica de Juego en Cuadrícula**
   - Manipulación de arreglos 2D
   - Conversión de sistemas de coordenadas
   - Algoritmos de recorrido de cuadrícula
   - Mapeo de posición a índice

4. **Gestión de Estados**
   - Seguimiento del estado del juego (no iniciado, jugando, ganado)
   - Máquinas de estado de cartas (oculta, mostrada, descubierta)
   - Implementación de lógica por turnos
   - Banderas booleanas para control del juego

5. **Programación Orientada a Eventos**
   - Manejo de eventos de clic del mouse
   - Procesamiento de eventos
   - Lógica de interacción con botones

6. **Temporización y Retrasos**
   - Mecánicas basadas en tiempo con `time.time()`
   - Ocultamiento retrasado de cartas
   - Control de tasa de fotogramas con `clock.tick()`
   - Implementación de retrasos sin bloqueo

7. **Algoritmos de Aleatorización**
   - Técnicas de mezcla de cartas
   - Generación de posiciones aleatorias
   - Garantía de distribución equitativa

8. **Diseño del Ciclo de Juego**
   - Estructura del ciclo de renderizado
   - Separación de actualización y renderizado
   - Gestión de FPS
   - Actualizaciones continuas del estado del juego

9. **Detección de Colisiones**
   - Colisión punto-rectángulo (`collidepoint`)
   - Validación de límites de cuadrícula
   - Detección del área de clic

10. **Renderizado Visual**
    - Carga y blitting de imágenes
    - Dibujo de rectángulos
    - Renderizado de texto
    - Orden de renderizado por capas

---

### 🎯 Habilidades Desarrolladas

Al estudiar y modificar este código, obtendrás experiencia práctica con:

✅ **Patrones de diseño de juegos** y arquitectura  
✅ **Gestión de memoria** en juegos de memorama  
✅ **Diseño de interfaz de usuario** para juegos en cuadrícula  
✅ **Validación de entrada** y manejo de errores  
✅ **Implementación de algoritmos** (mezcla, emparejamiento)  
✅ **Organización del código** con clases y funciones  

Este repositorio es perfecto para estudiantes que aprenden Pygame, fundamentos del desarrollo de videojuegos, o cualquier persona interesada en entender cómo funcionan programáticamente los clásicos juegos de memoria.

---

## 📄 Licencia

Este proyecto es de naturaleza educativa y está disponible para uso libre con fines de aprendizaje. Los logos de los equipos de fútbol son propiedad de sus respectivos dueños y se utilizan únicamente con fines educativos.

---

## 🤝 Contribuciones

Estudiantes y desarrolladores son bienvenidos a:
- Reportar errores
- Sugerir nuevas características o temáticas
- Enviar pull requests con mejoras
- Compartir estrategias de juego
- Agregar nuevas temáticas de cartas

---

## 📧 Contacto

**Carlos Gabriel Magallanes López**  
Correo: cgmagallanes23@gmail.com  

---

**⭐ ¡Si disfrutaste este juego o te resultó educativo, dale una estrella en GitHub!**

**🎮 ¡Buen juego!**
