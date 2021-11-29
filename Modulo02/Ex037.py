num = int(input('Digite um numero: '))

print('''Escolha uma das bases para conversão:
[1] Converter para BINARIO
[2] Conveter para OCTAL
[3] Converter para HEXADECIMAL''') 
resp = int(input('Sua opção: '))

if resp == 1:
    print('O numero {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif resp == 2:
    print('O numero {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif resp == 3:
    print('O numero {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!!!')



# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para 
# o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.