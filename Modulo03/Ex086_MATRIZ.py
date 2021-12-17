matriz = [[0,0,0], 
         [0,0,0], 
         [0,0,0]]

for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para L [{l}]  C [{c}]: '))
print('\nMatriz Final:')
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        print('\n'if c == 2 else '', end='')