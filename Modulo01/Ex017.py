import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

#hp = (co ** 2 + ca **2) ** (1/2) metodo convecional sem usar a biblioteca math

#utilizando a biblioteca math

hp = math.hypot(ca ,co)

print('A Hipotenusa vai medir {:.2f}'.format(hp))