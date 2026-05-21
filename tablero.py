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
                