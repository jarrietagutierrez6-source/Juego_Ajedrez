import pygame

# Configuración del temporizador (en segundos)
TIEMPO_INICIAL = 600  # 10 minutos por jugador


def formatear_tiempo(segundos):
    """Convierte segundos a formato MM:SS"""
    minutos = int(segundos // 60)
    segs = int(segundos % 60)
    return f"{minutos:02d}:{segs:02d}"


def actualizar_temporizador(turno, tiempo_blanco, tiempo_negro, delta_tiempo):
    """
    Actualiza el temporizador del jugador actual.
    Retorna: (tiempo_blanco, tiempo_negro, juego_terminado, ganador)
    """
    juego_terminado = False
    ganador = None
    
    if turno == 'blanco':
        tiempo_blanco -= delta_tiempo
        if tiempo_blanco <= 0:
            tiempo_blanco = 0
            juego_terminado = True
            ganador = "2"  # Negras ganan
    else:
        tiempo_negro -= delta_tiempo
        if tiempo_negro <= 0:
            tiempo_negro = 0
            juego_terminado = True
            ganador = "1"  # Blancas ganan
    
    return tiempo_blanco, tiempo_negro, juego_terminado, ganador


def dibujar_panel_info(screen, turno, tiempo_blanco, tiempo_negro, font_grande, font_normal, ancho, alto, panel_alto, tablero_size):
    """Dibuja el panel inferior con información del turno y temporizadores"""
    # Fondo del panel
    panel_y = tablero_size
    pygame.draw.rect(screen, (20, 20, 20), (0, panel_y, ancho, panel_alto))
    pygame.draw.line(screen, (50, 50, 50), (0, panel_y), (ancho, panel_y), 2)
    
    # Dividir el panel en dos secciones
    mitad = ancho // 2
    
    # === JUGADOR 1 (Blancas) - Izquierda ===
    color_fondo_j1 = (60, 120, 60) if turno == 'blanco' else (50, 50, 50)
    pygame.draw.rect(screen, color_fondo_j1, (10, panel_y + 10, mitad - 20, panel_alto - 20), border_radius=10)
    
    # Texto Jugador 1
    texto_j1 = font_grande.render("JUGADOR 1", True, (255, 255, 255))
    screen.blit(texto_j1, (20, panel_y + 15))
    
    texto_color_j1 = font_normal.render("(Blancas)", True, (200, 200, 200))
    screen.blit(texto_color_j1, (20, panel_y + 45))
    
    # Temporizador Jugador 1
    color_tiempo = (255, 100, 100) if tiempo_blanco < 60 else (255, 255, 255)
    texto_tiempo_j1 = font_grande.render(formatear_tiempo(tiempo_blanco), True, color_tiempo)
    screen.blit(texto_tiempo_j1, (mitad - 120, panel_y + 35))
    
    # Indicador de turno activo
    if turno == 'blanco':
        texto_turno = font_normal.render("TU TURNO", True, (255, 255, 0))
        screen.blit(texto_turno, (20, panel_y + 70))
    
    # === JUGADOR 2 (Negras) - Derecha ===
    color_fondo_j2 = (60, 120, 60) if turno == 'negro' else (50, 50, 50)
    pygame.draw.rect(screen, color_fondo_j2, (mitad + 10, panel_y + 10, mitad - 20, panel_alto - 20), border_radius=10)
    
    # Texto Jugador 2
    texto_j2 = font_grande.render("JUGADOR 2", True, (255, 255, 255))
    screen.blit(texto_j2, (mitad + 20, panel_y + 15))
    
    texto_color_j2 = font_normal.render("(Negras)", True, (200, 200, 200))
    screen.blit(texto_color_j2, (mitad + 20, panel_y + 45))
    
    # Temporizador Jugador 2
    color_tiempo = (255, 100, 100) if tiempo_negro < 60 else (255, 255, 255)
    texto_tiempo_j2 = font_grande.render(formatear_tiempo(tiempo_negro), True, color_tiempo)
    screen.blit(texto_tiempo_j2, (ancho - 120, panel_y + 35))
    
    # Indicador de turno activo
    if turno == 'negro':
        texto_turno = font_normal.render("TU TURNO", True, (255, 255, 0))
        screen.blit(texto_turno, (mitad + 20, panel_y + 70))


def mostrar_fin_tiempo(screen, ganador, ancho, alto):
    """Muestra mensaje cuando se acaba el tiempo"""
    overlay = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    font_grande = pygame.font.SysFont("Arial", 48, bold=True)
    font_normal = pygame.font.SysFont("Arial", 24)
    
    texto = f"JUGADOR {ganador} GANA"
    texto_surface = font_grande.render(texto, True, (255, 215, 0))
    rect = texto_surface.get_rect(center=(ancho // 2, alto // 2 - 30))
    screen.blit(texto_surface, rect)
    
    subtexto = "El tiempo del oponente se ha agotado"
    subtexto_surface = font_normal.render(subtexto, True, (255, 255, 255))
    rect2 = subtexto_surface.get_rect(center=(ancho // 2, alto // 2 + 20))
    screen.blit(subtexto_surface, rect2)
    
    instruccion = "Presiona ESPACIO para reiniciar o ESC para salir"
    instruccion_surface = font_normal.render(instruccion, True, (250, 250, 250))
    rect3 = instruccion_surface.get_rect(center=(ancho // 2, alto // 2 + 80))
    screen.blit(instruccion_surface, rect3)