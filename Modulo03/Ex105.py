
def notas(*numeros, sit = False):
    """
    Função para montar o dicionário.
    """
    import math
    dic = dict()
    dic['total'] = len(numeros)
    dic['maior'] = max(numeros)
    dic['menor'] = min(numeros)
    dic['média'] = sum(numeros) / len(numeros)

    if sit == True:
        if dic['média'] >= 5 and dic['média'] < 7:
            dic['situação'] = 'Razoavel'
        elif dic['média'] > 7:
            dic['situação'] = 'Boa'
        elif dic['média'] < 5:
            dic['situação'] = 'Ruim'

    return dic
#Programa principal
resp = notas(5.6,6.1,4.2,7.5, sit = True)
print(resp)
# print(help(notas))