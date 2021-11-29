import time
from datetime import date

tempo = date.today().year

print(tempo)
maior = 0
menor = 0
for i in range(1,8):
    nascimento = int(input('Em que ano você nasceu? '))
    ano = tempo - nascimento
    if ano < 18:
        print('Você é de menor')
        menor += 1

    else: 
        print('Você é de maior')
        maior+= 1

print(f'Ao todos existe {maior} pessoas maiores de idade e {menor} pessoas menores de idade')

'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
 mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''