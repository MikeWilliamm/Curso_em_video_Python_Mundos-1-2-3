#DECLARAÇÃO
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))

i = 11
qtdT = 0
while i != 0:
        for c in range(0,i):
            print(termo, end='')
            print(' -> ', end='')
            termo += razao
            qtdT += 1
        print('Pausa')
        i = int(input('\nQuantos termos quer ver ainda? '))

print(f'Progessão finalizada com {qtdT - 1} mostrados!')
