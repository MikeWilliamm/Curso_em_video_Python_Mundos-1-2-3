import Ex108_modulo

preco = float(input('Digite o preço: R$ '))
metade = Ex108_modulo.metade(preco)
dobro = Ex108_modulo.dobro(preco)
aumento = Ex108_modulo.aumento(preco)

print(f'A metade de {Ex108_modulo.moeda(preco)} é {Ex108_modulo.moeda(metade)}')
print(f'O dobro de {Ex108_modulo.moeda(preco)} é {Ex108_modulo.moeda(dobro)}')
print(f'{Ex108_modulo.moeda(preco)} com aumento de 10%, temos {Ex108_modulo.moeda(aumento)} ')