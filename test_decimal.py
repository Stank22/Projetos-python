
import unittest
from decimal import Decimal


class TestDecimais(unittest.TestCase):

    def test_decimais(self):
        resultado = Decimal('125.555')

        resultado = resultado.quantize(Decimal('0.01'))

        self.assertEqual(resultado, Decimal('125.56'))


if __name__ == '__main__':
    unittest.main()

import unittest
from decimal import Decimal


class TestDecimais(unittest.TestCase):

    def test_decimais(self):
        resultado = Decimal('125.555')

        resultado = resultado.quantize(Decimal('0.01'))

        self.assertEqual(resultado, Decimal('125.56'))


if __name__ == '__main__':
    unittest.main()
