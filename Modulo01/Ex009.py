n = int(input('Digite um numero para ver a tabuada: '))
print('\n')
print('Tabuado do {}:'.format(n))
print('-'*12)

for i in range(1,11):
    print("{} X {} = {}".format(n, i, n*i))

print('-'*12)