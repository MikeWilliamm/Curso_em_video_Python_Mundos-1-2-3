preco = float(input('Preço da compreas: R$'))
print('''Formas de pagamento:
[1] À vista
[2] À vista no cartão
[3] 2x no cartão
[4] 3X ou mais no cartão''')
opcao = int(input('Qual a opção: '))


if opcao == 1:
    desconto = (preco * 10) / 100
    valor = preco - desconto
    print ('Com pagamento a vista no DINHEIRO/CHEQUE sua compra terá 10''%'' de desconto.\nValor final = RS{}'.format(valor))
elif opcao == 2:
    desconto = (preco * 5) / 100
    valor = preco - desconto
    print('Com pagamento a vista no CARTÃO sua compra terá 5''%'' de desconto.\nValor final = RS{}'.format(valor))
elif opcao == 3:
    print('Pagando em 2x no CARTÃO preço normal R${}'.format(preco))
elif opcao == 4:
    juros = (preco * 20) / 100
    valor = preco + juros
    vezes = int(input('Em quantas vezes deseja parcelar? '))
    print('Pagando em {}x o preço ter 20''%'' de juros,\n O valor final é de {}'.format(vezes, valor))
else:
     print('Opção invalida!!!')





'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''