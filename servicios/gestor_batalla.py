import random
from modelos.enemigos import Slime, Dragon


class GestorBatalla:
    """Coordina las reglas de combate; no depende de la interfaz gráfica."""

    def __init__(self, jugador):
        self.jugador = jugador
        self.enemigo = None
        self.terminada = True

    def iniciar(self):
        self.enemigo = random.choice([Slime(), Dragon()])
        self.terminada = False
        return self.enemigo

    def turno_jugador(self):
        if self.terminada or self.enemigo is None:
            raise RuntimeError("Primero debes iniciar una batalla.")
        danio, descripcion = self.jugador.atacar()
        recibido = self.enemigo.recibir_danio(danio)
        if not self.enemigo.esta_vivo:
            self.terminada = True
            return [f"{descripcion} Daño: {recibido}.", "¡Victoria! Has derrotado al enemigo."]
        danio_enemigo, descripcion_enemigo = self.enemigo.atacar()
        recibido_jugador = self.jugador.recibir_danio(danio_enemigo)
        if not self.jugador.esta_vivo:
            self.terminada = True
        return [
            f"{descripcion} Daño: {recibido}.",
            f"{descripcion_enemigo} Daño recibido: {recibido_jugador}."
        ]

    def usar_pocion(self):
        if self.terminada:
            raise RuntimeError("No hay una batalla activa.")
        return self.jugador.curar(25)
