import unittest
from operacoes import somar, subtrair, multiplicar, dividir

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
       resultado = dividir(10, 0)
       self.assertEqual(resultado, 'Numero invalido')


    def test_somar_negativos(self):
        resultado = somar(-10, -5)
        self.assertEqual(resultado, -15)


    def test_multiplicar_por_zero(self):
        resultado = multiplicar (25, 0)
        self.assertEqual(resultado, 0)        

if __name__ == '__main__':
    unittest.main()
