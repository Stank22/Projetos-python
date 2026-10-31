import unittest

from calculos import realizar_calculo


class TestCalculos(unittest.TestCase):

    def test_realizar_soma(self):
        resultado = realizar_calculo('1', 2, 3)
        self.assertEqual(resultado, 5)

    def test_realizar_subtracao(self):
        resultado = realizar_calculo('2', 5, 3)
        self.assertEqual(resultado, 2)

    def test_realizar_multiplicacao(self):
        resultado = realizar_calculo('3', 4, 5)
        self.assertEqual(resultado, 20)

    def test_realizar_divisao(self):
        resultado = realizar_calculo('4', 10, 2)
        self.assertEqual(resultado, 5.0)