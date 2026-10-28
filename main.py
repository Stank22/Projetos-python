from operacoes import somar, subtrair, multiplicar, dividir


def mostrar_menu():
    print('''===== CALCULADORA =====
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair''')

print('CALCULADORA PYTHON XD')

while True:
    mostrar_menu()

    operacao = input('Escolha Operação:')
    if operacao == '0':
        break

    try:
        primeiro_numero = float(input('digite o primeiro numero:'))
        segundo_numero = float(input('digite o segundo numero:'))

    except ValueError:
        print('Erro: digite apenas numeros válidos')

    else: 
       def realizar_calculo(operacao, primeiro_numero, segundo_numero):
            if operacao == '1':
                resultado = somar(primeiro_numero, segundo_numero)
                return resultado

            elif operacao == '2':
                resultado = subtrair(primeiro_numero, segundo_numero)
                return resultado

            elif operacao == '3':
                resultado = multiplicar(primeiro_numero, segundo_numero)
                return resultado

            elif operacao == '4':
                resultado = dividir(primeiro_numero, segundo_numero)
                return resultado

            else:
                print('Operação inválida')
                return None
                resultado = dividir(primeiro_numero, segundo_numero)
                print(f'Resultado: {resultado}')
                except ValueError as e:
                print(f'Erro: {e}')

            else:
            print('Operação inválida')

    resposta = input('Deseja realizar outro cálculo? (s/n)').lower()

    if resposta == 'n':
        break

print('Calculadora encerrada.')