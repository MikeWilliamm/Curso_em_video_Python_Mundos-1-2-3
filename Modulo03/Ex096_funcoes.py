def area(l, c):
    a = l*c
    print(f'A área de um terreno {l}x{c} é igual {a}m2.')

print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area(largura, comprimento)

