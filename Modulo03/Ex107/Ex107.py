import Ex107_modulo

preco = float(input('Digite o preço: R$ '))
metade = Ex107_modulo.metade(preco)
dobro = Ex107_modulo.dobro(preco)
aumento = Ex107_modulo.aumento(preco)
print(f'A metade de R${preco:.2f} é R${metade:.2f}')
print(f'O dobro de R${preco:.2f} é R${dobro:.2f}')
print(f'{preco:.2f} com aumento de 10%, temos {aumento:.2f} ')