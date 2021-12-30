from time import sleep

def contagem(ini, fim, pas):
    if pas == 0:
        pas = 1
    if ini < 0 and pas <0 and ini < fim:
        pas = pas*-1
    print('-='*15)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}.')
    sleep(2.5)
    if ini < fim:
        for i in range(ini, fim+1, pas):
            print(i, end= ' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for i in range(ini, fim-1, pas):
            print(i, end= ' ', flush=True)
            sleep(0.5)
        print('FIM!')


contagem(1,10,1)
contagem(10, 0, -2)
print('Agora é sua vez de personalizar a contagem :D')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)