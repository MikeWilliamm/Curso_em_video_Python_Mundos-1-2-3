from datetime import date, datetime
import sys

ano = datetime.now().year

print(ano)

nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano - nascimento

if idade < 0:
    print('nascimento invalido')
    sys.exit()

if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta Senior')
else: 
    print('Atleta MASTER')

'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''