termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))

decimo = termo + (10*1) * razao #Formula para calcular o decimo termo de uma progressão aritimética.

for i in range(termo, decimo + razao , razao):
    print(f'{i}', end= ' -> ')
print('Acabou')