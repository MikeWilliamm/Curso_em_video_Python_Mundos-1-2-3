qtd18 = qtdH = qtdF = 0

while True:
    print('-'*20 + ' CADASTRE UMA PESSOA ' + '-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    while sexo != 'M' and  sexo != 'F':
        print('\nDigito invalido!!!')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    else:
        if idade > 18:
            qtd18 +=1

        if sexo == 'M':
            qtdH += 1

        if idade < 20 and sexo == 'F':
            qtdF += 1
    
    continuar  = str(input('\nQuer continuar? [S/N] ')).upper().strip()[0]

    while continuar not in 'SN':
        print('\nDigito invalido!!!')
        continuar  = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'\nTotal de pessoas com mais de 18 anos: {qtd18}')
print(f'Ao todo temos {qtdH} homens cadastrados')
print(f'e todo temos {qtdF} mulheres com menos de 20 anos')