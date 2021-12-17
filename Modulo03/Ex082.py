numeros = []
numeros_impares = []
numeros_pares = []
while True:

    numeros.append(int(input('Digite um numero: ')))

    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    while resp != 'S' and resp != 'N':
        print('Digito invalido!!!')
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    
    if resp == 'N':
        break

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros_pares.append(numeros[i])
    else:
        numeros_impares.append(numeros[i])

print(f'''A lista completa é: {numeros}
A lista de pares é {numeros_pares}
A lista de impares é {numeros_impares}''')