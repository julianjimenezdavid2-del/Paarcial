import unittest
from modelos.personajes import Guerrero, Mago
from modelos.enemigos import Slime
from servicios.gestor_batalla import GestorBatalla


class PruebasCombate(unittest.TestCase):
    def test_vida_no_baja_de_cero(self):
        slime = Slime()
        slime.recibir_danio(500)
        self.assertEqual(slime.vida, 0)
        self.assertFalse(slime.esta_vivo)

    def test_curacion_no_supera_vida_maxima(self):
        guerrero = Guerrero()
        guerrero.recibir_danio(40)
        guerrero.curar(500)
        self.assertEqual(guerrero.vida, guerrero.vida_maxima)

    def test_no_acepta_danio_negativo(self):
        mago = Mago()
        with self.assertRaises(ValueError):
            mago.recibir_danio(-5)

    def test_gestor_inicia_batalla(self):
        gestor = GestorBatalla(Guerrero())
        enemigo = gestor.iniciar()
        self.assertIn(enemigo.nombre, ["Slime", "Dragón"])
        self.assertFalse(gestor.terminada)


if __name__ == "__main__":
    unittest.main()
