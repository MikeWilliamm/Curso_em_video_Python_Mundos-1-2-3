#Tuplas são imultaveis, não é possivel alterar os seus valores ex: lanche[1] = 'Refrigerante, retornara erro
lanche = ('Hambuergue', 'Pizza', 'Suco', 'Pudim', 'batata frita')

#Fatiamento de tupla:

#mostra um elemento especifico da tupla
print(lanche[1])

#mostra um elemento especifico, o menos representa a contagem de elemento de tras para frente
print(lanche[-1])

#Fatia elementos da tupla, sempre mostrara o até o elemento anterior do final especificado
print(lanche[1:3]) #mostrara do elemento 1 até o 2

#mostra de um elemento especifico até o final da tupla
print(lanche[2:])

#mostra a tupla do inicio até um elemente anterior ao especificado
print(lanche[:2])

#for com tuplas: 

#for com range
for count in range(len(lanche)):
    print(f'Eu vou comer {lanche[count]}')
print('Comi d+')


#for com variavel composta
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi d+')

#for com variavel composta utilizando o enumerate para capturar o contador
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi d+')

#coloca em ordem a tupla
print(sorted(lanche))


#funções com tuplas:

#Fazendo junção de tuplas simples
tupla_a = (2,5,4)
tupla_b = (5,8,1,2)
tupla_C = tupla_a + tupla_b

print(tupla_a)
print(tupla_b)
print(tupla_C)

#printando os argumentos da tupla em ordem
print(sorted(tupla_C))

#contando quando elementos especificos existe na tupla
print(tupla_C.count(5))

#procura o primeiro elemento na tupla e mostra o seu indice
print(tupla_C.index(5))

#procura o primeiro elemento na tupla e mostra o seu indice a partir de um determinado index
print(tupla_C.index(5, 2)) #a partir da posição 2, pois o outro 5 está na posicão 1

