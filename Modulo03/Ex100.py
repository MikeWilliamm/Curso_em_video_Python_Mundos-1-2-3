import random
def sortea():
    print(f'Sorteando 5 valores da lista ', end = '')
    numeros = list()
    for i in range(0,5):
        num = random.randint(1,10)
        print(num, end=' ')
        numeros.append(num)
    print('Pronto.')
    
    
    return numeros
def soma(numeros):
    
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'\nSomando os valores pares de {numeros}, temos {soma}')

numeros = sortea()
soma(numeros)