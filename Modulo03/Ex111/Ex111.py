from Ex111.utilidades import moeda
"""
Funções:
    param 'preco': Valor de entrada do usuario.
    param 'True ou False': True = formatação da moeda | False = não formatação.
"""
preco = float(input('Digite o preço: R$ '))

moeda.resumo(preco, 20, 12)