valor = float(input('Digita o valor do salário de um funcionario: R$'))
valoraumento = float(input('Digite a porcetagem do aumento do salarío: %'))
aumento = (valor*valoraumento/100) + valor 

print('Um funcionario que ganhava R${:.2f} com 15% de aumento passara a ganhar R${:.2f}'.format(valor, aumento))