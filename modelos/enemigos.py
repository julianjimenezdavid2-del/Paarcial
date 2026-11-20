import random
from modelos.entidad import Combatiente


class Slime(Combatiente):
    def __init__(self):
        super().__init__("Slime", 65)

    def atacar(self) -> tuple[int, str]:
        return random.randint(7, 13), "El Slime salta y golpea."


class Dragon(Combatiente):
    def __init__(self):
        super().__init__("Dragón", 105)

    def atacar(self) -> tuple[int, str]:
        return random.randint(12, 21), "El Dragón lanza una llamarada."
