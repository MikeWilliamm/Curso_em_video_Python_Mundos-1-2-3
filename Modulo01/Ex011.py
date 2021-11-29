largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

print('Sua parede tem a dimenção de {} X {}, sua aréa é de {} metros cubicos'.format(largura, altura, area))
tinta = area / 2 #cada 2 metros quadrados gasta 2 litros de tinta
print('Para pintar essa parede será necessários {} litros de tinta'.format(tinta))