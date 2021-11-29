import random

print('Sou o seu computador...')

n = random.randint(1,10)
print('Acabei de pensar em um numeto entra 1 e 10.')
print('Você consegue adivinhar qual numero foi?')


n2 = 20
contador = 0
while n != n2:
    n2 = int(input('\nQual numero eu pensei? '))
    contador += 1
    if n < n2:
        print('Menos... Tente mais uma vez.')
    elif n > n2:
        print('Mais... Tente mais uma vez.')
        
print(f'VocÊ acertou com {contador} tentativas!')

