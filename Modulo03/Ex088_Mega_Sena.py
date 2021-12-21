import random
import time

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

qtd = int(input('Quantos jogos quer fazer: '))

print(f'{"-="*4 + " Sorteando jogos " + "=-"*4:^30}')

n = random.randint(1,60)

lista = []

for j in range(1,qtd+1):
    for i in range(1,7):
        n = random.randint(1,60)

        if n not in lista:
            lista.append(n)
        else:
            while n in lista:
                n = random.randint(1,60)
            lista.append(n)

        if i == 6:
            lista.sort()
            print(f'Jogo {j}: {lista}')
            time.sleep(0.3)
            lista.clear()

print(f'{"-="*5 + "< BOA SORTE >"+ "=-"*5:^30}')