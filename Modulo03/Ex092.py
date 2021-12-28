from datetime import date
cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['ano'] = int(input('Ano de Nascimento: '))
bkp = cadastro['ano']
data_atual = date.today()
cadastro['ano'] = data_atual.year - cadastro['ano'] 
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    
    cadastro['aposento'] = (cadastro['contratacao'] - bkp) + 35
    print()
    for k, v in cadastro.items():
        print(f'{str(k).capitalize()} tem o valor {v}')

else:
    print()
    for k, v in cadastro.items():
        print(f'{str(k).capitalize()} tem o valor {v}')

