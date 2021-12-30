def maior(*numeros):
    print('-='*20)
    print('Analisando os valores passados...')
    for i in numeros:
        print(f'{i} ', end = '')
    maiorr = 0 
    contador = 0
    for i in numeros:
        if contador == 0:
            maiorr = i
        elif i > maiorr:
            maiorr = i
        contador += 1
    if len(numeros) == 0:
        print(f'\nForam informados 0 valores ao todo')
        print(f'Não existe um maior valor')
    else:
        print(f'\nForam informados {len(numeros)} valores ao todo.')
        print(f'O maior valor é o {maiorr}.')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
maior(0)