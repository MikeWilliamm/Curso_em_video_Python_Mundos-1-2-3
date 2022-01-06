def cabecalho(msg, tam = 42):
    print('-'*tam)
    print(str(msg).center(tam))
    print('-'*tam)

def menu(lista):
    cabecalho('MEU PRINCIPAL')
    for c in range(len(lista)):
        print(f'\033[1;33m{c+1}\033[m - \033[1;34m{lista[c]}\033[m')

def leiaINT(n = False):    
    while True:
        try:
            if not n:
                resp = int(input('\033[1;33mSua opção: \033[m'))
                break
            elif n:
                resp = int(input('Sua Idade: '))
                break
        except (ValueError, TypeError):
            print('\033[1;31mERRO!!! Digite um valor inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mDigite um valor inteiro Valido.\033[m')
            continue
    return resp

    