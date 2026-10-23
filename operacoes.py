from decima import Decimal

def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero


def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero


def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero


def dividir(primeiro_numero, segundo_numero):
    if segundo_numero == 0:
        raise ValueError("Divisão por zero não é permitida.")
    else:
        return primeiro_numero / segundo_numero


def arredondar_valor(valor):
    valor = valor.quantize(Decimal('0.01'))
    return valor

