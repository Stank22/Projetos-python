
from calculos import realizar_calculo


def mostrar_menu():
    print('''===== CALCULADORA =====
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair''')


def main():
    print('CALCULADORA PYTHON XD')

    while True:
        mostrar_menu()

        operacao = input('Escolha a operação: ')

        if operacao == '0':
            break

        if operacao not in ('1', '2', '3', '4'):
            print('Operação inválida')
            continue

        try:
            primeiro_numero = float(input('Digite o primeiro número: '))
            segundo_numero = float(input('Digite o segundo número: '))

            resultado = realizar_calculo(
                operacao,
                primeiro_numero,
                segundo_numero
            )

            print(f'Resultado: {resultado}')

        except ValueError as e:
            print(f'Erro: {e}')

        resposta = input('Deseja realizar outro cálculo? (s/n): ').lower()

        if resposta == 'n':
            break

    print('Calculadora encerrada.')


if __name__ == '__main__':
    main()
