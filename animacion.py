import pygame
import random
import math
import os

# Intentar importar OpenCV para reproducir el video .mp4
try:
    import cv2
    CV2_DISPONIBLE = True
except ImportError:
    CV2_DISPONIBLE = False
    print("[Aviso] OpenCV no está instalado. Usa 'pip install opencv-python' para la animación de video.")


class Particula:
    """Una partícula individual de la explosión"""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        # Velocidad aleatoria en todas las direcciones
        angulo = random.uniform(0, 2 * math.pi)
        velocidad = random.uniform(2, 7)
        self.vx = math.cos(angulo) * velocidad
        self.vy = math.sin(angulo) * velocidad
        self.color = color
        self.radio = random.uniform(3, 7)
        self.vida = 1.0  # Vida de 1.0 a 0.0
        self.decaimiento = random.uniform(0.02, 0.04)

    def actualizar(self):
        """Mueve la partícula y reduce su vida"""
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15  # Gravedad
        self.vida -= self.decaimiento
        self.radio *= 0.97  # Se encoge poco a poco

    def dibujar(self, screen):
        """Dibuja la partícula con transparencia según su vida"""
        if self.vida > 0 and self.radio > 0.5:
            alpha = int(255 * self.vida)
            radio = int(self.radio)
            superficie = pygame.Surface((radio * 2, radio * 2), pygame.SRCALPHA)
            color_con_alpha = (*self.color, alpha)
            pygame.draw.circle(superficie, color_con_alpha, (radio, radio), radio)
            screen.blit(superficie, (int(self.x - radio), int(self.y - radio)))

    def esta_viva(self):
        return self.vida > 0 and self.radio > 0.5


class Explosion:
    """Una explosión completa formada por muchas partículas"""
    def __init__(self, x, y, color_principal=(255, 140, 0)):
        self.particulas = []
        # Colores de la explosión (naranjas, rojos y amarillos tipo fuego)
        colores = [
            (255, 200, 50),   # Amarillo
            (255, 140, 0),    # Naranja
            (255, 80, 0),     # Naranja rojizo
            (220, 40, 40),    # Rojo
            color_principal,
        ]
        # Crear entre 25 y 35 partículas
        cantidad = random.randint(25, 35)
        for _ in range(cantidad):
            color = random.choice(colores)
            self.particulas.append(Particula(x, y, color))

    def actualizar(self):
        """Actualiza todas las partículas y elimina las muertas"""
        for p in self.particulas:
            p.actualizar()
        self.particulas = [p for p in self.particulas if p.esta_viva()]

    def dibujar(self, screen):
        """Dibuja todas las partículas"""
        for p in self.particulas:
            p.dibujar(screen)

    def terminada(self):
        """Devuelve True cuando ya no quedan partículas"""
        return len(self.particulas) == 0


class GestorExplosiones:
    """Maneja todas las explosiones activas en el juego"""
    def __init__(self):
        self.explosiones = []

    def crear_explosion(self, fila, col, tamaño_celda, color=(255, 140, 0)):
        """Crea una explosión en el centro de una casilla"""
        x = col * tamaño_celda + tamaño_celda // 2
        y = fila * tamaño_celda + tamaño_celda // 2
        self.explosiones.append(Explosion(x, y, color))

    def actualizar(self):
        """Actualiza todas las explosiones y elimina las terminadas"""
        for explosion in self.explosiones:
            explosion.actualizar()
        self.explosiones = [e for e in self.explosiones if not e.terminada()]

    def dibujar(self, screen):
        """Dibuja todas las explosiones activas"""
        for explosion in self.explosiones:
            explosion.dibujar(screen)


class GestorVideo:
    """Maneja las animaciones de video al capturar piezas.

    Carga los fotogramas del video UNA SOLA VEZ y los reutiliza,
    para que no haya tirones al reproducir.
    """
    def __init__(self, ruta_video="video.mp4"):
        self.ruta_video = ruta_video
        self.animaciones = []
        self.frames_cache = None  # Fotogramas precargados
        self.disponible = CV2_DISPONIBLE and os.path.exists(ruta_video)

        # Precargar los fotogramas del video una sola vez
        if self.disponible:
            self.frames_cache = self._cargar_frames(ruta_video)
            if not self.frames_cache:
                self.disponible = False

    def _cargar_frames(self, ruta):
        """Lee el video y devuelve una lista de superficies (sin escalar)"""
        frames = []
        cap = cv2.VideoCapture(ruta)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = frame.swapaxes(0, 1)
            superficie = pygame.surfarray.make_surface(frame)
            frames.append(superficie)
        cap.release()
        return frames

    def crear_animacion(self, fila, col, tamaño_celda, escala=1.5):
        """Crea una animación de video en el centro de una casilla.

        escala > 1 hace el video un poco más grande que la casilla
        para que el efecto se vea más vistoso.
        """
        if not self.disponible:
            return
        x = col * tamaño_celda + tamaño_celda // 2
        y = fila * tamaño_celda + tamaño_celda // 2
        tamaño = int(tamaño_celda * escala)
        anim = {
            "frames": self.frames_cache,
            "indice": 0,
            "x": x,
            "y": y,
            "tamaño": tamaño,
        }
        self.animaciones.append(anim)

    def actualizar(self):
        """Avanza todas las animaciones y elimina las terminadas"""
        for anim in self.animaciones:
            anim["indice"] += 1
        self.animaciones = [a for a in self.animaciones if a["indice"] < len(a["frames"])]

    def dibujar(self, screen):
        """Dibuja el fotograma actual de cada animación activa"""
        for anim in self.animaciones:
            frame = anim["frames"][anim["indice"]]
            frame_escalado = pygame.transform.scale(frame, (anim["tamaño"], anim["tamaño"]))
            rect = frame_escalado.get_rect(center=(anim["x"], anim["y"]))
            screen.blit(frame_escalado, rect)
