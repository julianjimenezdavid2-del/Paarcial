from abc import ABC, abstractmethod


class Combatiente(ABC):
    """Clase abstracta que define el contrato de cualquier combatiente."""

    def __init__(self, nombre: str, vida_maxima: int):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if vida_maxima <= 0:
            raise ValueError("La vida máxima debe ser mayor que cero.")
        self.nombre = nombre
        self._vida_maxima = vida_maxima
        self._vida = vida_maxima

    @property
    def vida(self) -> int:
        return self._vida

    @property
    def vida_maxima(self) -> int:
        return self._vida_maxima

    @property
    def esta_vivo(self) -> bool:
        return self._vida > 0

    def recibir_danio(self, cantidad: int) -> int:
        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo.")
        danio_real = min(cantidad, self._vida)
        self._vida -= danio_real
        return danio_real

    def curar(self, cantidad: int) -> int:
        if cantidad < 0:
            raise ValueError("La curación no puede ser negativa.")
        curacion_real = min(cantidad, self._vida_maxima - self._vida)
        self._vida += curacion_real
        return curacion_real

    @abstractmethod
    def atacar(self) -> tuple[int, str]:
        """Devuelve el daño y una descripción del ataque."""
        raise NotImplementedError
