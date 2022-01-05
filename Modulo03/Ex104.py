def leiaint(frase):

   while True:
    n = str(input(f'{frase}'))
    if n.isnumeric():
        n = int(n)
        return n
        break
    else: 
        print('\033[0;31mERRO!!! Dígito invalido.\033[m')
        print(f'\033[0;31mVocê digitou "{n}".\033[m')

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o numero {n}.')
