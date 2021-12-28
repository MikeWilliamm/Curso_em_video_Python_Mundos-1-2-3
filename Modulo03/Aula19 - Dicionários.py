pessoas = {'nome': 'Mike',
            'sexo': 'M',
            'idade': 23}
print('Exemplo de print com um dicionario: ')
print(f'O {pessoas["nome"]} tem  {pessoas["idade"]} anos\n') #Exemplo de print com um dicionario 

print('- ''KEYS'' Mostra as cheves(indices) do dicionario ')
print(pessoas.keys())#Mostra as cheves(indices) do dicionario 
print('- ''values'' Mostra os valores do dicionario  ')
print(pessoas.values())#Mostra os valores do dicionario 
print('- ''items'' Mostra as cheves e os valores do dicionario  ')
print(pessoas.items())#Mostra as cheves e os valores do dicionario

#print utilizando o FOR
print()
print('print utilizando o FOR:')
print('- ''keys'' Printa chave a chave começando da primeira  ')
for k in pessoas.keys(): #printa chave a chave começando da primeira
    print(k)

print()
print('- ''values'' Printa valor a valor comecando do primeiro ')
for v in pessoas.values(): #printa valor a valor comecando do primeiro
    print(v)

print()
print('- ''items'' Printa chave e o valor')
for k, v in pessoas.items(): #printa chave e o valor, k = key | v = value
    print(f'KEY: {k} | VALOR: {v}')

print()
print('Deletando:')
print('- ''del'' apagando uma key do dicionario ')
del pessoas['sexo'] #apagando uma key do dicionario 
print(pessoas.keys())

print()
print('Criando um dicionario dentro de uma lista:')

brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado)
brasil.append(estado2)

print(brasil)

print()
print('Filtrando lista composta por um dicionario:')
print(brasil[1]['uf'])

print()
print('Exemplo prático: ')
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade federatica: '))
    estado['sigla'] = str(input('sigla: '))
    brasil.append(estado.copy())#da mesma forma da lista, que para que não fosse criado uma ligação era 
                                #necessário utilizar o 'lista[:]', para que seja feito uma copia do dicionario
                                #sem uma ligação é necessário utilizar o '.copy()'
    estado.clear()

for e in brasil: #FOR DA LISTA
    for k, v in e.items():#for do dicionario
        print(f'o campo {k} tem o valor {v}')