contador = 0
numeros = []
while True:
    contador += 1
    numeros.append(int(input('Digite um valor: ')))

    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while resp !=  'N' and resp != 'S':
        print('Digito invalido!!!')
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    
    if resp == 'N':
        break

numeros.sort(reverse=True)


print(f'''\nVocê digitou {contador} elementos.
Os valores em ordem decrescente são {numeros}.
''' + ('O valor 5 faz parte da lista!' if 5 in numeros else 'O valor 5 não faz parte da lista!'))
