def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero


def subtrair(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero


def multiplicar(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero


def dividir(primeiro_numero, segundo_numero):
    if segundo_numero != 0:
        return primeiro_numero / segundo_numero
    else:
        return "Numero invalido"
