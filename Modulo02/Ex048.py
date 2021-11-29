soma=0
count = 0
for i in range(1,501, 2):
    if i % 3 == 0:
        print(i, end=' ')
        soma = soma+i
        count = count +1
print(f'\nA soma de {count} nuneros multplos de 3 é {soma}')