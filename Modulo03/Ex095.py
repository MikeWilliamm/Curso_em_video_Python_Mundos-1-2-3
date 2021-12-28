jogadores = {}
lista_jogadores = []
contador = 0
while True:
    aux = []
    aux.clear()

    jogadores['id'] = contador
    jogadores['nome'] = str(input('Nome: '))

    qtd = int(input(f'Quantas partidas o {jogadores["nome"]} jogou? '))

    for i in range(1,qtd+1):
        aux.append(int(input(f'Quatos gols na partida {i}? ')))
    
    jogadores['gols'] = aux[:]

    jogadores['total'] = sum(aux)

    lista_jogadores.append(jogadores.copy())
    jogadores.clear()
    contador += 1
    
    print(lista_jogadores)

    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while resp[0] not in 'SN':
        print('Digito Errado!!!')
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    
    if resp[0] == 'N':
        break
print('-='*25)
print(f'{"cod":<6}{"Nome":<12}{"Gols":<20}{"Total":<12}')
print('-'*50)
for i in lista_jogadores:
    print(f'{i["id"]:>3}   {i["nome"]:<12}{str(i["gols"]):<20}{i["total"]:<12}')
print('-='*25)

while True:
    mostrar = int(input("Mostrar os dados de qual jogador? [999 para parar]: "))

    if mostrar == 999:
        print('<<< VOLTE SEMPRE >>>')
        break

    contador_if = 0
    verifica = 0
    for i in lista_jogadores:
        if mostrar == i["id"]:
            verifica = 1
            print(f' -- Levantamento do jogador {i["nome"]}:')
            contador_j = 1
            for j in i['gols']:
                print(f'    No jogo {contador_j} fez {j} gols')
                contador_j += 1
        contador_if += 1
        print()
        if contador_if == len(lista_jogadores) and verifica == 0:
            print(f'ERRO! Não existe jogador com o código {mostrar}!!!\n')

        