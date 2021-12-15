import random

n = tuple(random.randint(1,10) for i in range(5))

print('\nOs valores sorteados foram: ', end='')

for i in range(len(n)):
    print(n[i], end=' ')

print(f'\n\nO menor valor é {sorted(n)[0]}')
print(f'O maior valor é {sorted(n)[-1]}')

#outra forma de fazer
print(f'\nO menor valor é {min(n)}')
print(f'O maior valor é {max(n)}')