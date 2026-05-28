from turtle import Screen

import pygame

def tablero(pantalla, tamaño_celda):
    #colores del tablero
    Blanco = (255,255,255)
    Negro = (0,0,0)

    # declaramos filas y columnas 
    filas = 8
    columna = 8 

    for fila in range(filas):
        for col in range(columna):
            #colorear celda
            if(fila + col) % 2 == 0:
                color = Blanco
            else:
                color = Negro
                #dibujar la celda
                rect = (col * tamaño_celda, fila * tamaño_celda, tamaño_celda, tamaño_celda)
                pygame.draw.rect(pantalla, color, rect)
                
def resaltar_casilla(pantalla, fila, col, tamaño_celda, color=(100, 200, 100, 128)):
    """Resalta una casilla específica del tablero"""
    superficie = pygame.Surface((tamaño_celda, tamaño_celda), pygame.SRCALPHA)
    superficie.fill(color)
    pantalla.blit(superficie, (col * tamaño_celda, fila * tamaño_celda))


def obtener_casilla(pos_mouse, tamaño_celda):
    """Convierte posición del mouse a coordenadas del tablero (fila, columna)"""
    x, y = pos_mouse
    col = x // tamaño_celda
    fila = y // tamaño_celda
    if 0 <= fila < 8 and 0 <= col < 8:
        return (fila, col)
    return None
                
