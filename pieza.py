import pygame


class Pieza:
    def __init__(self, tipo, color, imagen, fila, col, tamaño_celda):
        """
        tipo: 'rey', 'reina', 'torre', 'alfil', 'caballo', 'peon'
        color: 'blanco' o 'negro'
        imagen: superficie de pygame con la imagen de la pieza
        fila, col: posición inicial en el tablero (0-7)
        tamaño_celda: tamaño de cada casilla del tablero
        """
        self.tipo = tipo
        self.color = color
        self.imagen = imagen
        self.fila = fila
        self.col = col
        self.tamaño_celda = tamaño_celda
        self.seleccionada = False
        self.primer_movimiento = True  # Para el peón (movimiento doble) y enroque

    def obtener_posicion_pixeles(self):
        """Devuelve la posición en píxeles para dibujar la pieza"""
        x = self.col * self.tamaño_celda + (self.tamaño_celda - self.imagen.get_width()) // 2
        y = self.fila * self.tamaño_celda + (self.tamaño_celda - self.imagen.get_height()) // 2
        return (x, y)

    def contiene_punto(self, pos):
        """Verifica si un punto (x, y) está dentro de la pieza"""
        x, y = self.obtener_posicion_pixeles()
        ancho = self.imagen.get_width()
        alto = self.imagen.get_height()
        px, py = pos
        return x <= px <= x + ancho and y <= py <= y + alto

    def mover_a(self, fila, col):
        """Mueve la pieza a una nueva posición"""
        self.fila = fila
        self.col = col
        self.primer_movimiento = False

    def obtener_movimientos_validos(self, tablero_piezas):
        """
        Devuelve una lista de movimientos válidos [(fila, col), ...]
        tablero_piezas: diccionario {(fila, col): Pieza}
        """
        movimientos = []

        if self.tipo == 'peon':
            movimientos = self._movimientos_peon(tablero_piezas)
        elif self.tipo == 'torre':
            movimientos = self._movimientos_torre(tablero_piezas)
        elif self.tipo == 'caballo':
            movimientos = self._movimientos_caballo(tablero_piezas)
        elif self.tipo == 'alfil':
            movimientos = self._movimientos_alfil(tablero_piezas)
        elif self.tipo == 'reina':
            movimientos = self._movimientos_reina(tablero_piezas)
        elif self.tipo == 'rey':
            movimientos = self._movimientos_rey(tablero_piezas)

        return movimientos

    def _es_casilla_valida(self, fila, col):
        """Verifica si la casilla está dentro del tablero"""
        return 0 <= fila < 8 and 0 <= col < 8

    def _es_casilla_vacia(self, fila, col, tablero_piezas):
        """Verifica si una casilla está vacía"""
        return (fila, col) not in tablero_piezas

    def _es_enemigo(self, fila, col, tablero_piezas):
        """Verifica si hay una pieza enemiga en la casilla"""
        if (fila, col) in tablero_piezas:
            return tablero_piezas[(fila, col)].color != self.color
        return False

    def _movimientos_peon(self, tablero_piezas):
        movimientos = []
        # Dirección según el color (blanco sube, negro baja)
        direccion = -1 if self.color == 'blanco' else 1

        # Movimiento hacia adelante (1 casilla)
        nueva_fila = self.fila + direccion
        if self._es_casilla_valida(nueva_fila, self.col):
            if self._es_casilla_vacia(nueva_fila, self.col, tablero_piezas):
                movimientos.append((nueva_fila, self.col))

                # Movimiento doble desde posición inicial
                if self.primer_movimiento:
                    nueva_fila_doble = self.fila + 2 * direccion
                    if self._es_casilla_vacia(nueva_fila_doble, self.col, tablero_piezas):
                        movimientos.append((nueva_fila_doble, self.col))

        # Capturas diagonales
        for delta_col in [-1, 1]:
            nueva_col = self.col + delta_col
            if self._es_casilla_valida(nueva_fila, nueva_col):
                if self._es_enemigo(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))

        return movimientos

    def _movimientos_torre(self, tablero_piezas):
        movimientos = []
        # Direcciones: arriba, abajo, izquierda, derecha
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for df, dc in direcciones:
            for i in range(1, 8):
                nueva_fila = self.fila + df * i
                nueva_col = self.col + dc * i

                if not self._es_casilla_valida(nueva_fila, nueva_col):
                    break

                if self._es_casilla_vacia(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))
                elif self._es_enemigo(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))
                    break
                else:
                    break  # Pieza aliada bloquea

        return movimientos

    def _movimientos_caballo(self, tablero_piezas):
        movimientos = []
        # Movimientos en L
        saltos = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        for df, dc in saltos:
            nueva_fila = self.fila + df
            nueva_col = self.col + dc

            if self._es_casilla_valida(nueva_fila, nueva_col):
                if self._es_casilla_vacia(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))
                elif self._es_enemigo(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))

        return movimientos

    def _movimientos_alfil(self, tablero_piezas):
        movimientos = []
        # Direcciones diagonales
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for df, dc in direcciones:
            for i in range(1, 8):
                nueva_fila = self.fila + df * i
                nueva_col = self.col + dc * i

                if not self._es_casilla_valida(nueva_fila, nueva_col):
                    break

                if self._es_casilla_vacia(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))
                elif self._es_enemigo(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))
                    break
                else:
                    break

        return movimientos

    def _movimientos_reina(self, tablero_piezas):
        # La reina combina los movimientos de torre y alfil
        return self._movimientos_torre(tablero_piezas) + self._movimientos_alfil(tablero_piezas)

    def _movimientos_rey(self, tablero_piezas):
        movimientos = []
        # El rey se mueve 1 casilla en cualquier dirección
        direcciones = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]

        for df, dc in direcciones:
            nueva_fila = self.fila + df
            nueva_col = self.col + dc

            if self._es_casilla_valida(nueva_fila, nueva_col):
                if self._es_casilla_vacia(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))
                elif self._es_enemigo(nueva_fila, nueva_col, tablero_piezas):
                    movimientos.append((nueva_fila, nueva_col))

        return movimientos

    def dibujar(self, pantalla):
        """Dibuja la pieza en la pantalla"""
        pos = self.obtener_posicion_pixeles()
        pantalla.blit(self.imagen, pos)
