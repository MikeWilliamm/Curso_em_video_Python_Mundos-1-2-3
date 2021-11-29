soma = 0
count = 0
count2 = 0
for i in range(1,7):
    num = int(input('Digite um valor: '))
    if num %2 ==0:
        soma += num
        count += 1
    count2 += 1
print(f'Soma de numeros pares= {soma}')
print(f'Contador de numeros pares = {count}')
print(f'Contador de todos numeros digitados = {count2}')