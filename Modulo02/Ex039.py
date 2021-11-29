from datetime import date
import sys


sexo = str(input('\nSe você for do sexo masculino digite a letra M, se for do sexo feminino digite F: ')).upper()
if sexo == 'F':
    print('Você não é obrigada a fazer o alistamento militar!')
    resp = str(input('Deseja se alistar(S/N)?')).upper()
    if resp == 'N':
        print('Tenha um bom dia!')
        sys.exit()
    elif resp != 'S':
        print('Digito invalido!')
        sys.exit()
elif sexo == 'M':
    print('Você é obrigado a fazer o alistamento militar!')
else:
    print('Digito invlido!!!')
    sys.exit()

data_atual = date.today()
ano = str(data_atual)[0:4]
ano = int(ano)



nascimento = int(input('Digite seu ano de nascimento: '))
tempo = ano - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, tempo, ano))
if tempo > 18:
    print('Seu alistamento foi em {}'.format((ano) - (tempo-18)))
elif tempo < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-tempo))
else:
    print('Voce deve se alistar imediatamente')
    
    





'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''