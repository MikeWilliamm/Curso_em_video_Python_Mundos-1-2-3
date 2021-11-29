casa = float(input('\nQual valor da casa? '))
salario = float(input('\nQual valor do salario? '))
anos = int(input('\nEm Quantos anos vai pagar? '))

parcelas = casa / (anos * 12) 
porcentagem = (salario * 30) / 100

if parcelas > porcentagem:
    print('\nPara comprar uma casa de {} a prestação será de R${:.2f} em {}x vezes\nEmprestimo Negado!\nA prestação mensal não pode exceder 30''%'' do salário!'.format(casa, parcelas, anos * 12))
elif parcelas <= porcentagem:
    print('\nPara comprar uma casa de {} a prestação será de R${:.2f} em {}x vezes\nEmprestimo Aprovado!'.format(casa, parcelas, anos * 12))

#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.