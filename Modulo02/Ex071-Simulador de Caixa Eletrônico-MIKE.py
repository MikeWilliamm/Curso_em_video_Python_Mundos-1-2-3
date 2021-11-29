# Fundamento: pegar o valor que deseja sacar, dividir pelo valor da nota, pegar apenas a parte inteira
#da divisão, essa parte será o quantidade de notas. Para verificar as outras notas basta, fazer o valor
#que deseja ser sacado - a quantidade de notas que já foi sacada na primeira operação.
# Esse novo valor de sacar deve passar pelo mesmo processo em toda verificação de emissão de nota!
print('='*30)
print('{:^30}'.format('Banco Mike'))
print('='*30)

qtd50 = qtd20 = qtd10 = qtd5 =0

sacar = float(input('\nQual valor que sacar? R$ '))



if sacar >= 50:
    qtd50 = int(sacar/50)
    sacar = sacar - (50 * qtd50)
    print(f'Total de cedulas de 50: {qtd50}')

if sacar >= 20:
    qtd20 = int(sacar/20)
    sacar = sacar - (20 * qtd20)
    print(f'Total de cedulas de 20: {qtd20}')

if sacar >= 10:
    qtd10 = int(sacar/10)
    sacar = sacar - (10 * qtd10)
    print(f'Total de cedulas de 10: {qtd10}')

if sacar >= 5:
    qtd5 = int(sacar/5)
    sacar = sacar - (5 * qtd5)
    print(f'Total de cedulas de 5: {qtd5}')

if sacar >= 1:
    qtd1 = int(sacar / 1)
    sacar = sacar - (1 * qtd1)
    print(f'Total de cedulas de 1: {qtd1}')

if sacar > 0:
    print(f'Não foi possivel sacar R${sacar}!')

print('Volte sempre ao banco MIKE, tenha um bom dia!')
