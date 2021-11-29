for i in range(1,7): #para iniciar contagem em 1, sempre o for parara no segundo parametro 
    print(f'{i} Olá for')
print('FIM')


for i in range(0,7, 2): #pulando de dois em dois
    print(f'{i} Olá for regressivo')
print('FIM')

for i in range(6,0, -1): #for regressivo
    print(f'{i} Olá for regressivo')
print('FIM')

n = int(input('Digite um numero: '))

for i in range(1,n+1):
    print(f'{i}')