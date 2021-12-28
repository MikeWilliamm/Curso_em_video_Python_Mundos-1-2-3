dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Média de {dic["nome"]}: '))

print('-=' * 30)


if dic['media'] >= 5 and dic['media'] < 7:
    dic['situacao'] = 'Recuperação'
elif dic['media'] <5:
    dic['situacao'] = 'Reprovado'
elif dic['media'] >= 7:
    dic['situacao'] = 'Aprovado'

for k, v in dic.items():
    print(f'{k} é igual a {v}')