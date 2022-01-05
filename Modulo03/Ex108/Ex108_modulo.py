def metade(preco):
    return preco / 2

def dobro(preco):
    return preco *2

def aumento(preco):
    aumento = preco + ((preco * 10) /100)
    return aumento

def moeda(preco = 0, moeda = 'R$'):
    return str(f'{moeda}{preco:>.2f}').replace('.', ',')