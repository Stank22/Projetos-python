
import unittest
from operacoes import somar, subtrair, multiplicar, dividir
from decimal import Decimal, arredondar_valor

class TestOperacoes(unittest.TestCase):

    def test_somar(self):
        resultado = somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_subtrair(self):
        resultado = subtrair(20, 8)
        self.assertEqual(resultado, 12)

    def test_multiplicar(self):
        resultado = multiplicar(7, 6)
        self.assertEqual(resultado, 42)

    def test_dividir(self):
        resultado = dividir(20, 4)
        self.assertEqual(resultado, 5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_somar_negativos(self):
        resultado = somar(-10, -5)
        self.assertEqual(resultado, -15)

    def test_multiplicar_por_zero(self):
        resultado = multiplicar(25, 0)
        self.assertEqual(resultado, 0)

    def test_somar_varios_valores(self):
        casos = [
            (10, 5, 15),
            (-10, -5, -15),
            (0, 0, 0),
            (-10, 5, -5),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = somar(a, b)
                self.assertEqual(resultado, esperado)

    def test_multiplicar_varios_valores(self):
        casos = [
            (5, 5, 25),
            (10, 0, 0),
            (-4, 3, -12),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = multiplicar(a, b)
                self.assertEqual(resultado, esperado)

    def test_dividir_varios_valores(self):
        casos = [
            (20, 4, 5),
            (15, 3, 5),
            (-20, 5, -4),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = dividir(a, b)
                self.assertEqual(resultado, esperado)

    def test_dividir_decimais(self):
        casos = [
            (1, 3, 0.3333333),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                resultado = dividir(a, b)
                self.assertAlmostEqual(resultado, esperado)

    def test_arredondar_valor(self):
        valor = Decimal('150.998')
        esperado = Decimal('151.00')
        
        resultado = arredondar_valor(resultado)
        self.assertEqual(resultado, esperado)
        

if __name__ == '__main__':
    unittest.main()
