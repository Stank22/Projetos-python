from main import realizar_calculo

def test_realizar_calculo():
    # Teste de soma
    assert realizar_calculo('1', 2, 3) == 5
    # Teste de subtração
    assert realizar_calculo('2', 5, 3) == 2
    # Teste de multiplicação
    assert realizar_calculo('3', 4, 5) == 20
    # Teste de divisão
    assert realizar_calculo('4', 10, 2) == 5.0
    # Teste de operação inválida
    assert realizar_calculo('5', 1, 1) is None



