print('CALCULADORA PYTHON XD')


while True: 
    try:
        primeiro_numero = float(input('digite o primeiro numero:'))
        segundo_numero = float(input('digite o segundo numero:'))

    except ValueError:
        print('Erro: digite apenas numeros válidos')

    else: 
        operacao = input('Escolha Operação:')
        if operacao == '1':
            resultado = primeiro_numero + segundo_numero
            print(f'Resultado: {resultado}')
        elif operacao == '2':
            resultado = primeiro_numero - segundo_numero
            print(f'Resultado: {resultado}')  
        elif operacao == '3':
            resultado = primeiro_numero * segundo_numero
            print(f'Resultado: {resultado}')
        elif operacao == '4':
            if segundo_numero != 0:
                resultado = primeiro_numero / segundo_numero
                print(f'Resultado: {resultado}')
            else:
                print('Erro: Divisão por zero não é permitida.')
        else:
            print('Operação inválida')       
    resposta = input('Deseja realizar outro cálculo? (s/n)').lower()

    if resposta == 'n':
        break
print('Calculadora encerrada.')