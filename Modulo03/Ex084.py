pessoas = []
aux = []

while True:

    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    pessoas.append(aux[:])
    aux.clear()

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp != 'N' and resp != 'S':
        print('Digito invalido!!!')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()

    if resp == 'N':
        break



maiorp = 0
menorp = 0

for i in range(len(pessoas)):
    if i == 0:
        maiorp = pessoas[i][1]
        menorp = pessoas[i][1]
    else:
        if pessoas[i][1] > maiorp:
            maiorp = pessoas[i][1]
        if pessoas[i][1] < menorp:
            menorp = pessoas[i][1]


    

print(f'\nAo todo você cadastrou {len(pessoas)} pessoas.')
print(f'\nO Maior peso foi de {maiorp}Kg. Peso de ', end = '')
for i in pessoas:
    if i[1] == maiorp:
        print(f'[{i[0]}]', end=' ')




print(f'\nO Menor peso foi de {menorp}Kg. Peso de ', end = '')
for i in range(len(pessoas)):
    if pessoas[i][1] == menorp:
        print(f'[{pessoas[i][0]}]', end = ' ')

