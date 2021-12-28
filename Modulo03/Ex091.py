from random import randint
from time import sleep
from operator import itemgetter
num_list = {'jogardor1': randint(1,6), 'jogardor2': randint(1,6), 'jogardor3': randint(1,6), 'jogardor4': randint(1,6)}

print('Valores Sorteados: ')
# print(num_list)

for k, v in num_list.items():
    print(f' o {k} tirou {v}.')
    sleep(0.5)

ranking = list()
ranking = sorted(num_list.items(), key = itemgetter(1), reverse=True)

print('\nRanking:')
for i, v in enumerate(ranking):
    print(f' o {i+1} lugar: {v[0]} com {v[1]}.')
    sleep(0.5)