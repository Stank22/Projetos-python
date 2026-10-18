print('Programa iniciado')

while True:
    resposta = input('Deseja continuar ? (s/n)').lower()
    
    if resposta == 's':
        print('Perguntar novamente')
    elif resposta == 'n':
        break
    else:  
        print('Opção Invalida')
print('Programa encerrado')