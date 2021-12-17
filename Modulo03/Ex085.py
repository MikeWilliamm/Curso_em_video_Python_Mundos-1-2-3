num = [[], []]

valor = 0

for i in range (1,8):
    valor = int(input(f'Digite {i} valor: '))
    if valor % 2 == 0 :
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-'*30)

num[0].sort()
num[1].sort()
print(f'Lista completa: {num}')
print(f'Numeros pares: {num[0]}')
print(f'Numeros impares: {num[1]}')