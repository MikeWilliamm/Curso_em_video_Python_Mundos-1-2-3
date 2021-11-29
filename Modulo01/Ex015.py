dias = int(input('Digite a quantidade de dias alugados: '))
kms = float(input('Digite a quantidade de kms rodados: '))

valor = (dias * 60) + (kms * 0.15)

print('O veiculo foi alugado por {} dias e rodou {} kms, o valor total a se pagar é de R${:.2f}'.format(dias, kms, valor))