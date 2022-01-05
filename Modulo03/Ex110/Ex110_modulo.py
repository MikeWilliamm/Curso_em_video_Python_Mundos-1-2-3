def metade(preco, formato = False):
    res = preco / 2
    return res if formato == False else moeda(res)

def dobro(preco, formato = False):
    res = preco *2
    return res if formato == False else moeda(res)

def aumento(preco, aument, formato = False):
    res = preco + ((preco * aument) /100)
    return res if formato == False else moeda(res)

def reduzir(preco, porcet, formato = False):
    res = preco - ((preco * porcet) /100)
    return res if formato == False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return str(f'{moeda}{preco:>.2f}').replace('.', ',')

def resumo(preco = 0, aument = 10, reducao = 5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado:  \t{moeda(preco):<12}')
    print(f'Metade do preço:  \t{metade(preco, True):<12}')
    print(f'Dobro do preço:  \t{dobro(preco, True):<12}')
    print(f'{aument}% de aumento:  \t{aumento(preco, aument, True):<12} ')
    print(f'{reducao}% de redução:  \t{reduzir(preco, reducao, True):<12}')
    print('-'*30)