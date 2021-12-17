#Fazendo uma copia da lista utilizando list_name[:], se os ':' não forem utilizados, será feito um replicação da lista onde existira um ligação com a antiga lista.
teste = list()
teste.append('Mike')
teste.append(23)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(teste)
print(galera)

#Acessando valores de um lista composta(lista dentro de outra lista)
print('=-'*30)
galera = [['joao', 22], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]

print(galera)
print(galera[2][1]) #será retornado o indice 0 da lista, e dentro do indice 0 será retornado o indice 0

for p in galera:
    print(p[0]) #printara todos os indices 0 dentro da lista composta

print()

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade') #print utilizando lista composta
print()

#Entrada de dados de uma lista composta:
print('=-'*30)
galera = list()
dado = []

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Não se esquecer dos ':', para que seja feito uma copia sem ligação com a lista anterior.
    dado.clear()

print(f'Galera: {galera}')

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} possui mais que 21 anos!')
