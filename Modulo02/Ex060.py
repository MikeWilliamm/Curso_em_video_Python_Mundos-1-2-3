import math
# f = math.factorial(num)

# Método WHILE
num = int(input('Digite um numero para calcular o seu fatorial: '))
c = num
f = 1
print(f'Calculando {num} FATORIAL! = ', end = '')
while c > 0:
    print(f'{c}', end = '')
    print(' x '  if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
    
print(f)

# Método FOR

num2 = int(input('\nDigite um numero para calcular o seu fatorial: '))
f2 = num2
for i in range(num2, 0, -1 ):
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end = '')

for j in range(1, num2):
    f2 *= j
print(f'Calculando {num2} FATORIAL! = {f2}')
