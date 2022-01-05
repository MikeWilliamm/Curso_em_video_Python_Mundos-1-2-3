import math
def ficha(nome = '<desconhecido>', g = 0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

print('-'*30)
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Quantidade de gol(s): ')).strip()

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))