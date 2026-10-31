from operacoes import somar, subtrair, multiplicar, dividir


def realizar_calculo(operacao, primeiro_numero, segundo_numero):
    if operacao == '1':
        return somar(primeiro_numero, segundo_numero)

    elif operacao == '2':
        return subtrair(primeiro_numero, segundo_numero)

    elif operacao == '3':
        return multiplicar(primeiro_numero, segundo_numero)

    elif operacao == '4':
        return dividir(primeiro_numero, segundo_numero)