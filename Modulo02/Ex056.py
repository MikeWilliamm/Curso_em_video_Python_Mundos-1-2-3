import sys
media = 0

homemvelho = ''
idademaior = 0

mulhermenor = 0
for i in range(1,5):
    print(f'----- Pessoa {i} -----')
    nome = str(input('\nDigite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo(M/F): ')).strip().upper()

    media += idade
    if sexo != 'M' and sexo != 'F' or idade < 0:
        print('\nArgumento invalido!!!\nInicie o programa novamente!')
        sys.exit()
        
    if i == 1:
        idademaior = idade
        homemvelho = nome
    else:
        if idade > idademaior and sexo == 'M':
            idademaior = idade
            homemvelho = nome
        if idade < 20 and sexo == 'F':
            mulhermenor+=1

media = media /4
print()
print(f'A média de idade é de {media} anos')
print(f'O Homem mais velho tem {idademaior} anos e seu nome é {homemvelho}')
print(f'Existe {mulhermenor} mulheres menores que 20 anos')