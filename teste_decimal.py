from decimal import Decimal


salario = Decimal('2500.567')
bonus = Decimal('350.256')


total = salario + bonus
total.quantize(Decimal('0.01'))
print(f'Resultado: {total}')