#lÊ 4 valor e guarda em uma tupla


from pandas.core import indexes


num = (int(input('Digite um numero: ' )), int(input('Digite um numero: ' )), int(input('Digite um numero: ' )),
        int(input('Digite um numero: ' )), int(input('Digite um numero: ' )) )

print(num)

#contado numeros 9  com for e contado
contador9 = 0
for i in range(len(num)):
    if num[i] == 9:
        contador9 +=1

print(f'\nExiste {contador9} numeros 9 na tupla')

#contando numeros 9 com o count
print(f'Existe {num.count(9)} numeros 9 na tupla')

try:
    print(f'\nO primeiro numero 3 foi encontrado no index: {num.index(3)}')
except:
    print('\nNão existe o numero 3 na lista')

print('\nNumeros pares da tupla:')
for i in range(len(num)):
    if num[i] % 2 == 0:
        print(num[i], end = '')
        print( ' | ' if i < len(num)-1 else '', end = '' )