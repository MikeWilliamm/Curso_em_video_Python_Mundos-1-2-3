jogador  =  dict()
jogador['nome'] = str(input('Nome do jogador: '))
qtd = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
aux = list()
for i in range(0,qtd):
    aux.append(int(input(f'Quantos gols na partida {i}: ')))

jogador['gols'] = aux
jogador['total'] = sum(aux)
print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {qtd} partidas:')
contador = 0

for i in range(qtd):
    print(f'    => Na partida {i}, fez {jogador["gols"][i]}')
print(f'Foi um total de {jogador["total"]} gols.')