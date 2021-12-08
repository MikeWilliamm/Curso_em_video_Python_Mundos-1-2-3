nm_numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
'dezoito', 'dezenove', 'vinte')



numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)


continuar = ''

while True:
    resp = int(input('Digite um numero entre de 0 até 20: '))
    while resp <0 or resp > 20:
        print('Digito invalido!')
        resp = int(input('Digite um numero de 0 até 20: '))

    for i in numeros:
        if i == resp:
            print(f'Você digitou o numero {nm_numeros[i]}')
    
    continuar = str(input('Você quer continuar [S/N]?')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Você quer continuar [S/N]?')).strip().upper()
    
    if  continuar == 'N':
        break

print('Programa finalizado!')