def helper(param):
    a = (f'Acessando o manual do comando {param}')
    num = int(len(a))
    print('\033[1;44m~'*(len(a) + 4))
    print(f' {a} ')
    print('\033[1;44m~\033[m'*(len(a) + 4))
    print('\033[1;30m\033[1;107m')
    print(help(param))
    print('\033[m')
while True:
    print('\033[1;42m~\033[m'*30)
    print(f'\033[1;42m{"SISTEMA DE AJUDA PYHELP":^30}\033[m')
    print('\033[1;42m~\033[m'*30)
    resp = str(input('Função ou biblioteca > '))
    if resp == 'fim':
        print('\033[1;41m')
        print('~'*30)
        print(f'{"PROGRAMA FINALIZADO":^30}')
        print('~'*30)
        print('\033[m')
        break
    else:
        helper(resp)