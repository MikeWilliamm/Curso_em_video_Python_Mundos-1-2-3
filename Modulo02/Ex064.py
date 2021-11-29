num = 0
contador = 0
soma = 0
num = int(input('Digite um numero [999 para PARAR]: '))
while num != 999: 
    
    contador += 1
    soma += num
    num = int(input('Digite um numero [999 para PARAR]: '))

print(f'Você digitou {contador} vezes e a soma de todos os numeros é {soma}')