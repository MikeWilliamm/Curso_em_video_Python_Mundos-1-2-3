cadastro = dict()
print(f'{"-="*10:<10}{" CADASTRO DE PESSOAS "}{"=-"*10:>10}')
cadastro_list = list()
contador = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while cadastro['sexo'] != 'M' and cadastro['sexo'] != 'F':
        print('Digito invalido!!!')
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    cadastro['idade'] = int(input('Idade: '))

    cadastro_list.append(cadastro.copy())
    cadastro.clear()

    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while resp != 'N' and resp != 'S':
        print('Digito invalido!!!')
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    contador += 1
    if resp == 'N':
        break
    
media = 0
contador = 0
mulheres = []

for i in cadastro_list:
    media += i['idade']

    if i['sexo'] == 'F':
        mulheres.append(i['nome'])

    contador += 1
    if contador == len(cadastro_list):
        media = media / contador 
print(media)        
 
pessoas = []

for i in cadastro_list:
    if i['idade'] > media:
        pessoas.append(i)

print(pessoas)
print(f'''\nA) Ao todo temos {contador} pessoas cadastradas!
B) A média de idade é igual a {media:.1f}
C) As mulheres cadastradas são: {str(mulheres).replace('[','').replace(']','').replace("'",'')}
D) Lista de pessoas que está acima da média: ''')

for i in pessoas:
    print(f"    {str(i).replace('[','').replace(']','').replace('{','').replace('}','')}")