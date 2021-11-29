num = int(input('Digiteo um numero inteiro: '))


unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Analisando o numero {}!\n'.format(num))

print('{} unidades'.format(unidade))
print('{} dezenas'.format(dezena))
print('{} centena'.format(centena))
print('{} milhar'.format(milhar))