pessoas = {'nome': 'Mike',
            'sexo': 'M',
            'idade': 23}

print(f'O {pessoas["nome"]} tem  {pessoas["idade"]} anos') #Exemplo de print com um dicionario 

print(pessoas.keys())#Mostra as cheves(indices) do dicionario 
print(pessoas.values())#Mostra os valores do dicionario 
print()
print(pessoas.items())#Mostra as cheves e os valores do dicionario

#print utilizando o FOR
print()
for k in pessoas.keys(): #printa chave a chave começando da primeira
    print(k)

for v in pessoas.values(): #printa valor a valor comecando do primeiro
    print(v)

for k, v in pessoas.items(): #printa chave e o valor 
    print(f'KEY: {k} | VALOR: {v}')

print()

del pessoas['sexo'] #apagando uma key do dicionario 
print(pessoas.keys())