frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

print(len(junto))
for i in range(len(junto) -1, -1, -1):
    
    inverso += junto[i]

print(f'Junto: {junto} \nInverso: {inverso}')
# print(f'Voce digitou a frase {junto}')

if junto == inverso:
    print(f'{frase} é uma palindromo!')
else:
    print(f'{frase} NÃO é uma palindromo!')
