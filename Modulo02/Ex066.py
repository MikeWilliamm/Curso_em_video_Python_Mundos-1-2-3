valor = contador = soma = 0

while True:
    valor = int(input('Digite um valor [999 para PARAR]: '))
    if valor == 999:
        break
    else:
        soma += valor
        contador += 1
print(f'A soma dos {contador} numeros é igual a {soma}')
