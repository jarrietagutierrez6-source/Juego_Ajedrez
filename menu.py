# Crear mi entorno virtual en python ejecutando el siguiente comando en la terminal:
# python -m venv mi_entorno
# Activar el entorno virtual:
# En Windows:
# mi_entorno\Scripts\activate.ps1
#instalar pygame en el entorno virtual:
# pip install pygame
#importamos pygame y sys para manejar eventos y salir del juego
import pygame
import sys
from pygame.locals import *
from tablero import tablero, resaltar_casilla, obtener_casilla
from pieza import Pieza
from temporizador import (
    TIEMPO_INICIAL,
    actualizar_temporizador,
    dibujar_panel_info,
    mostrar_fin_tiempo
)

#Crear mi repositorio en GitHub y subir mi proyecto a GitHub debe ser publico.
#Enviar Link de mi proyecto de GitHub al docente.


# Configuración

TAMAÑO_CELDA = 75
TAMAÑO_PIEZA = 65
TABLERO_SIZE = TAMAÑO_CELDA * 8  # 680 pixels (el tablero de 8x8)
PANEL_ALTO = 100  # Altura del panel inferior
ANCHO = TABLERO_SIZE  # 680
ALTO = TABLERO_SIZE + PANEL_ALTO  # 780 (tablero + panel debajo)

# Configuración del temporizador (en segundos)
TIEMPO_INICIAL = 600  # 10 minutos por jugador

def cargar_imagen(ruta):
    """Carga y escala una imagen de pieza"""
    try:
        imagen = pygame.image.load(ruta)
        return pygame.transform.scale(imagen, (TAMAÑO_PIEZA, TAMAÑO_PIEZA))
    except pygame.error:
        # Si no se encuentra la imagen, crear un placeholder
        superficie = pygame.Surface((TAMAÑO_PIEZA, TAMAÑO_PIEZA), pygame.SRCALPHA)
        pygame.draw.circle(superficie, (200, 50, 50), (TAMAÑO_PIEZA//2, TAMAÑO_PIEZA//2), TAMAÑO_PIEZA//3)
        return superficie


def crear_piezas():
    """Crea todas las piezas en sus posiciones iniciales"""
    piezas = []

    # Cargar imágenes (ajusta los nombres según tus archivos)
    img_torre_n = cargar_imagen("castiilo1.png")
    img_caballo_n = cargar_imagen("cab3.png")
    img_alfil_n = cargar_imagen("alfil3 (2).png")
    img_reina_n = cargar_imagen("reina3.png")
    img_rey_n = cargar_imagen("Rey3.png")
    img_peon_n = cargar_imagen("Peon1.png")

    # Para las piezas blancas usa las mismas imágenes o carga otras si las tienes
    img_torre_b = cargar_imagen("castiilo1.png")
    img_caballo_b = cargar_imagen("cab3.png")
    img_alfil_b = cargar_imagen("alfil3 (2).png")
    img_reina_b = cargar_imagen("reina3.png")
    img_rey_b = cargar_imagen("Rey3.png")
    img_peon_b = cargar_imagen("Peon1.png")

    # === PIEZAS NEGRAS (fila 0 y 1) ===
    # Fila 0: piezas principales negras
    piezas.append(Pieza('torre', 'negro', img_torre_n, 0, 0, TAMAÑO_CELDA))
    piezas.append(Pieza('caballo', 'negro', img_caballo_n, 0, 1, TAMAÑO_CELDA))
    piezas.append(Pieza('alfil', 'negro', img_alfil_n, 0, 2, TAMAÑO_CELDA))
    piezas.append(Pieza('reina', 'negro', img_reina_n, 0, 3, TAMAÑO_CELDA))
    piezas.append(Pieza('rey', 'negro', img_rey_n, 0, 4, TAMAÑO_CELDA))
    piezas.append(Pieza('alfil', 'negro', img_alfil_n, 0, 5, TAMAÑO_CELDA))
    piezas.append(Pieza('caballo', 'negro', img_caballo_n, 0, 6, TAMAÑO_CELDA))
    piezas.append(Pieza('torre', 'negro', img_torre_n, 0, 7, TAMAÑO_CELDA))

    # Fila 1: peones negros
    for col in range(8):
        piezas.append(Pieza('peon', 'negro', img_peon_n, 1, col, TAMAÑO_CELDA))

    # === PIEZAS BLANCAS (fila 6 y 7) ===
    # Fila 6: peones blancos
    for col in range(8):
        piezas.append(Pieza('peon', 'blanco', img_peon_b, 6, col, TAMAÑO_CELDA))

    # Fila 7: piezas principales blancas
    piezas.append(Pieza('torre', 'blanco', img_torre_b, 7, 0, TAMAÑO_CELDA))
    piezas.append(Pieza('caballo', 'blanco', img_caballo_b, 7, 1, TAMAÑO_CELDA))
    piezas.append(Pieza('alfil', 'blanco', img_alfil_b, 7, 2, TAMAÑO_CELDA))
    piezas.append(Pieza('reina', 'blanco', img_reina_b, 7, 3, TAMAÑO_CELDA))
    piezas.append(Pieza('rey', 'blanco', img_rey_b, 7, 4, TAMAÑO_CELDA))
    piezas.append(Pieza('alfil', 'blanco', img_alfil_b, 7, 5, TAMAÑO_CELDA))
    piezas.append(Pieza('caballo', 'blanco', img_caballo_b, 7, 6, TAMAÑO_CELDA))
    piezas.append(Pieza('torre', 'blanco', img_torre_b, 7, 7, TAMAÑO_CELDA))

    return piezas


def obtener_tablero_piezas(piezas):
    """Crea un diccionario {(fila, col): pieza} para consultas rápidas"""
    return {(p.fila, p.col): p for p in piezas}


def obtener_pieza_en_posicion(piezas, fila, col):
    """Devuelve la pieza en una posición específica o None"""
    for pieza in piezas:
        if pieza.fila == fila and pieza.col == col:
            return pieza
    return None


def main():
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Ajedrez - Pygame")
    clock = pygame.time.Clock()

    # Crear las piezas
    piezas = crear_piezas()

    # Estado del juego
    pieza_seleccionada = None
    movimientos_validos = []
    turno = 'blanco'  # Empiezan las blancas
    juego_terminado = False
    ganador = None

    # Temporizadores (en segundos)
    tiempo_blanco = TIEMPO_INICIAL
    tiempo_negro = TIEMPO_INICIAL
    ultimo_tick = pygame.time.get_ticks()

    # Fuentes
    font_grande = pygame.font.SysFont("Arial", 28, bold=True)
    font_normal = pygame.font.SysFont("Arial", 18)

    while True:
        # Calcular delta time para el temporizador
        tick_actual = pygame.time.get_ticks()
        delta_tiempo = (tick_actual - ultimo_tick) / 1000.0  # Convertir a segundos
        ultimo_tick = tick_actual

        # Actualizar temporizador del jugador actual (solo si el juego no ha terminado)
        if not juego_terminado:
            tiempo_blanco, tiempo_negro, juego_terminado, ganador = actualizar_temporizador(
                turno, tiempo_blanco, tiempo_negro, delta_tiempo
            )

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Teclas para reiniciar o salir
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE and juego_terminado:
                    # Reiniciar juego
                    piezas = crear_piezas()
                    pieza_seleccionada = None
                    movimientos_validos = []
                    turno = 'blanco'
                    tiempo_blanco = TIEMPO_INICIAL
                    tiempo_negro = TIEMPO_INICIAL
                    juego_terminado = False
                    ganador = None
                    ultimo_tick = pygame.time.get_ticks()

            if event.type == MOUSEBUTTONDOWN and not juego_terminado:
                pos_mouse = pygame.mouse.get_pos()
                casilla = obtener_casilla(pos_mouse, TAMAÑO_CELDA)

                if casilla:
                    fila, col = casilla
                    pieza_clickeada = obtener_pieza_en_posicion(piezas, fila, col)

                    # Si hay una pieza seleccionada y se clickea en un movimiento válido
                    if pieza_seleccionada and (fila, col) in movimientos_validos:
                        # Verificar si hay una pieza enemiga para capturar
                        pieza_capturada = obtener_pieza_en_posicion(piezas, fila, col)
                        if pieza_capturada:
                            piezas.remove(pieza_capturada)

                        # Mover la pieza
                        pieza_seleccionada.mover_a(fila, col)
                        pieza_seleccionada.seleccionada = False
                        pieza_seleccionada = None
                        movimientos_validos = []

                        # Cambiar turno
                        turno = 'negro' if turno == 'blanco' else 'blanco'

                    # Si se clickea en una pieza propia, seleccionarla
                    elif pieza_clickeada and pieza_clickeada.color == turno:
                        # Deseleccionar pieza anterior
                        if pieza_seleccionada:
                            pieza_seleccionada.seleccionada = False

                        # Seleccionar nueva pieza
                        pieza_seleccionada = pieza_clickeada
                        pieza_seleccionada.seleccionada = True
                        tablero_piezas = obtener_tablero_piezas(piezas)
                        movimientos_validos = pieza_seleccionada.obtener_movimientos_validos(tablero_piezas)

                    # Si se clickea en otro lugar, deseleccionar
                    else:
                        if pieza_seleccionada:
                            pieza_seleccionada.seleccionada = False
                        pieza_seleccionada = None
                        movimientos_validos = []

        # === DIBUJAR ===
        screen.fill((50, 50, 50))

        # Dibujar tablero
        tablero(screen, TAMAÑO_CELDA)

        # Resaltar casilla de pieza seleccionada
        if pieza_seleccionada:
            resaltar_casilla(screen, pieza_seleccionada.fila, pieza_seleccionada.col,
                           TAMAÑO_CELDA, (255, 255, 0, 100))  # Amarillo

        # Resaltar movimientos válidos
        for fila, col in movimientos_validos:
            pieza_en_destino = obtener_pieza_en_posicion(piezas, fila, col)
            if pieza_en_destino:
                # Casilla con pieza enemiga (captura) - rojo
                resaltar_casilla(screen, fila, col, TAMAÑO_CELDA, (255, 100, 100, 150))
            else:
                # Casilla vacía - verde
                resaltar_casilla(screen, fila, col, TAMAÑO_CELDA, (100, 255, 100, 150))

        # Dibujar piezas
        for pieza in piezas:
            pieza.dibujar(screen)

        # Dibujar panel de información con turnos y temporizadores
                # Dibujar panel de información debajo del tablero
        dibujar_panel_info(screen, turno, tiempo_blanco, tiempo_negro, font_grande, font_normal, ANCHO, ALTO, PANEL_ALTO, TABLERO_SIZE)

        # Mostrar pantalla de fin de juego si el tiempo se acabó
        if juego_terminado:
            mostrar_fin_tiempo(screen, ganador, ANCHO, ALTO)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

