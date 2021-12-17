valores = []

while True:
    valor = (int(input('Digite um valor: ')))

    if valor in valores:
        print('Valor duplicado! Não vou adicionar!')
    else:
        print('Valor adicionado na lista!')
        valores.append(valor)

    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while resp != 'N' and resp != 'S':
        print('\nDigito Invalido!')
        resp = str(input('Deseja continuar [S/N]? ')).upper().strip()
    
    if resp == 'N':
        break
valores.sort()
print(f'Você digitou os valores: ', end = '')
for i in range(len(valores)):
    print(f'{valores[i]}', end = '')
    print(' - ' if  i < len(valores)-1 else '', end = '')