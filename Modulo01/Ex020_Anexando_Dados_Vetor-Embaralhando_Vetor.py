import random



nomes = []
for i in range(0,4):
    nome = str(input('Nome: '))
    nomes.append(nome)

print(nomes)

print('\n' + '-'*40)

random.shuffle(nomes)


print("A ordem de apresentação será: {}".format(nomes))
