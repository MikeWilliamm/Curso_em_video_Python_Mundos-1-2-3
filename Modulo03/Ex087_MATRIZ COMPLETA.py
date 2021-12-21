matriz = [[0,0,0],[0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f' L [{l}] C [{c}] = '))

print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        print('\n' if c == 2 else '', end='')
print('=-'*30)

soma_par = 0
soma_3coluna = 0
maior_da_2linha = 0
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]

        if c == 2:
            soma_3coluna += matriz[l][c]
        
        if l == 1 and c == 0:
            maior_da_2linha = matriz[l][c]
        else: 
            if matriz[l][c] > maior_da_2linha:
                maior_da_2linha = matriz[l][c]

print(f'''A soma dos valores pares da matris é {soma_par}
A soma da terceira coluna é {soma_3coluna}
O maior valor da segunda linha é {maior_da_2linha}''')

#  L [0] C [0] = 3
#  L [0] C [1] = 2
#  L [0] C [2] = 6
#  L [1] C [0] = 5
#  L [1] C [1] = 1
#  L [1] C [2] = 9
#  L [2] C [0] = 7
#  L [2] C [1] = 4
#  L [2] C [2] = 2