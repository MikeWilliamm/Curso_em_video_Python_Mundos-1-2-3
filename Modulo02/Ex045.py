import random

num = random.randint(1,3)



escolha = int(input('''Escolha uma opção: 
[1] PEDRA
[2] PAPEL
[3] TESOURA

Qual a opçã? '''))
print('\n')
print('Escollha do computador: {}'.format(num))
print('\n')

if num == 1 and escolha == 3:
    print('O computador escolheu PEDRA e você TESOURA!\nVocê perdeu!!!')
elif num == 2 and escolha == 1:
    print('O computador escolheu PAPEL e você PEDRA!\nVocê perdeu!!!')
elif num == 3 and escolha == 2:
    print('O computador escolheu TESOURA e você PAPEL!\nVocê perdeu!!!')
elif escolha == 1 and num == 3:
    print('O computador escolheu TESOURA e você PEDRA!\nVocê Venceu!!!')
elif escolha == 2 and num == 1:
    print('O computador escolheu PEDRA e você PAPEL!\nVocê Venceu!!!')
elif escolha == 3 and num == 2:
    print('O computador escolheu PAPEL e você TESOURA!\nVocê Venceu!!!')
elif escolha == num:
    print('Você e o computador escolheream a mesma opção.\nIMPATE!!!')
else: 
    print('Escolha incorreta!!!')