
def leiaint():

    while True:
        try:
            inteiro = int(input('Digite um Inteiro: '))
        except ValueError:
            print('\033[1;31mERRO: Por favor, digite um número inteiro valido!\033[m')
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar esse numero\nNumero Inteiro = 0')
            inteiro = 0
            break
        else:
            break
    return inteiro

def leiareal():
    while True:
        try:
            real = float(input('Digite um Real: '))
        except ValueError:
            print('\033[1;31mERRO: Por favor, digite um número real valido!\033[m')
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar esse numero\nNumero Real = 0')
            real = 0
            break
        else:
            break
    return real   

inteiro = leiaint()
real = leiareal()     
print(f'O valor Inteiro é {inteiro} e o valor Real é {real}!')