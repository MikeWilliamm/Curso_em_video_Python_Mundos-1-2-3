a = float(input('digite o primeiro valor'))
b = float(input('digite o segundo'))
c = float(input('digite o último'))
if a<b+c and b<a+c and c<a+b:
    print('será possivel sim, fazer um triângulo')
    if a==b==c:
         print('equilatero')
    elif a != b != c != a:
        print('escaleno')
    else:
         print('isosceles')
else:
    print('não formará um triângulo')
'''
– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

