valor = float(input('Digite o valor do produto: R$'))

desconto = (valor*5)/100
valorfinal = valor - desconto

print('O produto que custa R${} com 5''%'' de desconto ira custar R${:.2f}'.format(valor, valorfinal))