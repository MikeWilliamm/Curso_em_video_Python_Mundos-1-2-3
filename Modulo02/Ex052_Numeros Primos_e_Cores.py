num = int(input('\033[mDigite um numero: '))#\033[m Denifi a cor 

tot = 0 
count = 0
for i in range(1, num+1):
    #print(i, end=' ')

    if num % i == 0:
        print('\033[34m', end = ' ') #se o numero for divisivel então a cor será azul
        tot += 1
    else:
        print('\033[m', end = ' ')
    print(f'{i}', end=' ')


print(f'\033[m\n\nO numero {num} foi divido {tot} vezes')
if tot == 2:#verifica se o numero é primo!
        print(f'\033[34mO numero {num} é primo!')
else:
        print(f'\033[mO numero {num} não é primo!')