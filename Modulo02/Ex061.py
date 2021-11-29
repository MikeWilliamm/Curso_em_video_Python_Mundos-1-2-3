#DECLARAÇÃO
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))



# FOR
resp = termo
for i in range(1,11): 
    print(resp, end = '')
    print(' -> ' if i < 10 else ' = ', end='')
    resp += razao
print('FIM\n')

#WHILE
aux = 0
resp2 = termo
while aux < 10:
    print(resp2, end='')
    print(' -> ' if aux < 9 else ' = ', end = '')
    aux += 1
    resp2 += razao
print('FIM')