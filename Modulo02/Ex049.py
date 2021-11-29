n = float(input('Digite um numero: '))

for i in range(1,11):
    print(f'{round(n,2)} X {i} = {round(i*n,0)}')