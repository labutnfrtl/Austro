import unittest
import re
from hardware.arduino import leer_datos

class TestArduinoLectura(unittest.TestCase):
    def test_formato_general(self):
        datos = leer_datos()

        self.assertIsInstance(datos, list)
        self.assertGreaterEqual(len(datos), 1)

        for linea in datos:
            self.assertIsInstance(linea, str)
            linea = linea.strip()

            # No debe comenzar ni terminar con punto y coma
            self.assertFalse(linea.startswith(";"), msg="La línea comienza con ';'")
            self.assertFalse(linea.endswith(";"), msg="La línea termina con ';'")

            partes = linea.split(";")

            for valor in partes:
                # Acepta enteros o decimales, positivos o negativos
                self.assertRegex(
                    valor,
                    r"^-?\d+(\.\d+)?$",
                    msg=f"Valor inválido: {valor}"
                )

if __name__ == '__main__':
    unittest.main()
