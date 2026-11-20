import random
from modelos.entidad import Combatiente


class Guerrero(Combatiente):
    def __init__(self, nombre: str = "Guerrero"):
        super().__init__(nombre, 120)

    def atacar(self) -> tuple[int, str]:
        danio = random.randint(16, 25)
        return danio, f"{self.nombre} realiza un golpe de espada."


class Mago(Combatiente):
    def __init__(self, nombre: str = "Mago"):
        super().__init__(nombre, 90)

    def atacar(self) -> tuple[int, str]:
        danio = random.randint(20, 30)
        return danio, f"{self.nombre} lanza una bola de energía."
