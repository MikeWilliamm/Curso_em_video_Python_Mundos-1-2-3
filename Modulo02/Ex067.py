
while True:
    num = int(input('Quer ver a tabuade de qual valor? '))

    if num < 0:
        break

    for i in range (1,11):
        print(f'{num} X {i} = {num*i}')
print('PROGRAMA DE TABUADA ENCERRADO! VOLTE SEMPRE.')