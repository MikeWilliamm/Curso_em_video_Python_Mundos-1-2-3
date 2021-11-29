import random

contador = 0
print('='*20 ,'VAMOS JOGAR PAR OU IMPAR', '='*20)

while True:

    comput = random.randint(0,11)
    jogador = int(input('Digite um valor: '))
    soma = comput + jogador

    PouI = str(input('Par ou Impar (P/I)? ')).upper().strip()[0]

    aux = 0

    if soma % 2 == 0:
        #print('O numero é par')
        aux = 'P'
        print(f'Você jogou {jogador} e o computador jogou {comput}. Total é {soma}. Deu PAR')
    else:
        aux = 'I'
        print(f'Você jogou {jogador} e o computador jogou {comput}. Total é {soma}. Deu IMPAR')

    if PouI == aux[0]:
        print('Você Venceu!\nJogue novamente :)')
        contador +=1
    else:
 
        break

print(f'\nGAME OVER! Você venceu {contador} vezes')
