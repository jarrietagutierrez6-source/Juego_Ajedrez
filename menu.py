# Crear mi entorno virtual en python ejecutando el siguiente comando en la terminal:
# python -m venv mi_entorno
# Activar el entorno virtual:
# En Windows:
# mi_entorno\Scripts\activate.ps1

#instalar pygame en el entorno virtual:
# pip install pygame

#importamos pygame y sys para manejar eventos y salir del juego
from sre_constants import BRANCH
from token import RARROW

import pygame, sys 
from pygame.locals import *
from tablero import*
#Crear mi repositorio en GitHub y subir mi proyecto a GitHub debe ser publico.
#Enviar Link de mi proyecto de GitHub al docente.

def main():
    pygame.init()
    ANCHO = 680
    ALTO = 680
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mi primer juego en Python")
    clock = pygame.time.Clock()
    imagen_pieza1 = pygame.image.load("castillo.png")
    imagen_pieza2 = pygame.image.load("reina.png")
    imagen_pieza3 = pygame.image.load("cab.png")
    imagen_pieza4 = pygame.image.load("alfin (1).png")
    imagen_pieza5 = pygame.image.load("rey.png")
    imagen_pieza6 = pygame.image.load("alfin (1).png")
    imagen_pieza7 = pygame.image.load("cab.png")
    imagen_pieza8 = pygame.image.load("castillo.png")
    imagen_pieza9 = pygame.image.load("peon.png")
    imagen_pieza10 = pygame.image.load("peon.png")
    imagen_pieza11 = pygame.image.load("peon.png")
    imagen_pieza12 = pygame.image.load("peon.png")
    imagen_pieza13 = pygame.image.load("peon.png")
    imagen_pieza14 = pygame.image.load("peon.png")
    imagen_pieza15 = pygame.image.load("peon.png")
    imagen_pieza16 = pygame.image.load("peon.png")
    imagen_pieza17 = pygame.image.load("castillo.png")
    imagen_pieza18 = pygame.image.load("cab.png")
    imagen_pieza19 = pygame.image.load("alfin (1).png")
    imagen_pieza20 = pygame.image.load("rey.png")
    imagen_pieza21 = pygame.image.load("reina.png")
    imagen_pieza22 = pygame.image.load("alfin (1).png")
    imagen_pieza23 = pygame.image.load("cab.png")
    imagen_pieza24 = pygame.image.load("castillo.png")
    imagen_pieza25 = pygame.image.load("peon.png")
    imagen_pieza26 = pygame.image.load("peon.png")
    imagen_pieza27 = pygame.image.load("peon.png")
    imagen_pieza28 = pygame.image.load("peon.png")
    imagen_pieza29 = pygame.image.load("peon.png")
    imagen_pieza30 = pygame.image.load("peon.png")
    imagen_pieza31 = pygame.image.load("peon.png")
    imagen_pieza32 = pygame.image.load("peon.png")

    imagen_pieza1 = pygame.transform.scale(imagen_pieza1, (75, 75))
    imagen_pieza2 = pygame.transform.scale(imagen_pieza2, (75, 75))
    imagen_pieza3 = pygame.transform.scale(imagen_pieza3, (75, 75))
    imagen_pieza4 = pygame.transform.scale(imagen_pieza4, (75, 75))
    imagen_pieza5 = pygame.transform.scale(imagen_pieza5, (75, 75))
    imagen_pieza6 = pygame.transform.scale(imagen_pieza6, (75, 75))
    imagen_pieza7 = pygame.transform.scale(imagen_pieza7, (75, 75))
    imagen_pieza8 = pygame.transform.scale(imagen_pieza8, (75, 75))
    imagen_pieza9 = pygame.transform.scale(imagen_pieza9, (75, 75))
    imagen_pieza10 = pygame.transform.scale(imagen_pieza10, (75, 75))
    imagen_pieza11 = pygame.transform.scale(imagen_pieza11, (75, 75))
    imagen_pieza12 = pygame.transform.scale(imagen_pieza12, (75, 75))
    imagen_pieza13 = pygame.transform.scale(imagen_pieza13,(75, 75))
    imagen_pieza14 = pygame.transform.scale(imagen_pieza14, (75, 75))
    imagen_pieza15 = pygame.transform.scale(imagen_pieza15, (75, 75))
    imagen_pieza16 = pygame.transform.scale(imagen_pieza16, (75, 75))
    imagen_pieza17 = pygame.transform.scale(imagen_pieza17, (75, 75))
    imagen_pieza18 = pygame.transform.scale(imagen_pieza18, (75, 75))
    imagen_pieza19 = pygame.transform.scale(imagen_pieza19, (75, 75))
    imagen_pieza20 = pygame.transform.scale(imagen_pieza20, (75, 75))
    imagen_pieza21 = pygame.transform.scale(imagen_pieza21, (75, 75))
    imagen_pieza22 = pygame.transform.scale(imagen_pieza22, (75, 75))
    imagen_pieza23 = pygame.transform.scale(imagen_pieza23, (75, 75))
    imagen_pieza24 = pygame.transform.scale(imagen_pieza24, (75, 75))
    imagen_pieza25 = pygame.transform.scale(imagen_pieza25, (75, 75))
    imagen_pieza26 = pygame.transform.scale(imagen_pieza26, (75, 75))
    imagen_pieza27 = pygame.transform.scale(imagen_pieza27, (75, 75))
    imagen_pieza28 = pygame.transform.scale(imagen_pieza28, (75, 75))
    imagen_pieza29 = pygame.transform.scale(imagen_pieza29, (75, 75))
    imagen_pieza30 = pygame.transform.scale(imagen_pieza30, (75, 75))
    imagen_pieza31 = pygame.transform.scale(imagen_pieza31, (75, 75))
    imagen_pieza32 = pygame.transform.scale(imagen_pieza32, (75, 75))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill((255, 255, 255))
        #pygame.draw.circle(screen, (15, 32, 30), (42, 45,), 30)
        # pygame.draw.circle(screen, (2, 200, 90), (212, 45), 30)
        #pygame.draw.circle(screen, (255, 32, 30), (380, 45), 30)
        font = pygame.font.SysFont("Arial", 30)
        mitexto = font.render("", True, RARROW)

        text_rect = mitexto.get_rect()
        text_rect.center = (ANCHO // 2, ALTO // 2)
        screen.blit(mitexto, text_rect)
        tablero(screen,85)
        screen.blit(imagen_pieza1, (5, 5))  # esquina superior izquierda
        screen.blit(imagen_pieza2, (345, 5))
        screen.blit(imagen_pieza3, (90, 5))
        screen.blit(imagen_pieza4, (179, 5))
        screen.blit(imagen_pieza5, (260, 5))
        screen.blit(imagen_pieza6, (430, 5))
        screen.blit(imagen_pieza7, (510, 5))
        screen.blit(imagen_pieza8, (600, 5))
        screen.blit(imagen_pieza9, (5, 90))
        screen.blit(imagen_pieza10, (85, 90))
        screen.blit(imagen_pieza11, (175, 90))
        screen.blit(imagen_pieza12, (260, 90))
        screen.blit(imagen_pieza13, (345, 90))
        screen.blit(imagen_pieza14, (430, 90))
        screen.blit(imagen_pieza15, (515, 90))
        screen.blit(imagen_pieza16, (602, 90))
        screen.blit(imagen_pieza17, (5, 600))
        screen.blit(imagen_pieza18, (85, 600))
        screen.blit(imagen_pieza19, (175, 600))
        screen.blit(imagen_pieza20, (260, 600))
        screen.blit(imagen_pieza21, (345, 600))
        screen.blit(imagen_pieza22, (430, 600))
        screen.blit(imagen_pieza23, (515, 600))
        screen.blit(imagen_pieza24, (602, 600))
        screen.blit(imagen_pieza25, (5, 515))
        screen.blit(imagen_pieza26, (90, 515))
        screen.blit(imagen_pieza27, (175, 515))
        screen.blit(imagen_pieza28, (260, 515))
        screen.blit(imagen_pieza29, (345, 515))
        screen.blit(imagen_pieza30, (430, 515))
        screen.blit(imagen_pieza31, (515, 515))
        screen.blit(imagen_pieza32, (602, 515))

        
        pygame.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
 main()