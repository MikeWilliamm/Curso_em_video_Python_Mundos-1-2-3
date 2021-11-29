import time

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

menu = 10

while menu != 0:
    time.sleep(0.5)
    print('-='*20)
    menu = int(input('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior
[4] Escolher novo numeros
[0] Sair do programa\n

Qual a opção? '''))

    if menu != 1 and menu != 2 and menu !=3 and menu !=4 and menu != 0:
        print('\nDigito invalido! Digite novamente!')
    elif menu == 0:
        print('Fim do Programa!')
        break
    elif menu == 1:
        print('A soma é: ')
        print(f'{n1} + {n2} = {n1+n2}')
    elif menu == 2:
        print('A multplicação é: ')
        print(f'{n1} X {n2} = {n1*n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior numero é {n1}!')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior numero é {n2}!')
        else:
            print(f'Os numeros digitados {n1} e {n2} são iguais!')
    elif menu == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))