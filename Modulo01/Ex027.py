nome = str(input('Digite seu nome: ')).strip().upper().split()

print('Seu primeiro nome é: {}'.format(nome[0].title()))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1].title()))

print('-'*20)

nome = ' '.join(nome) #uni todas a string que foi desunida pelo split, utilizando um ' '  para separar
posicao = nome.rfind(' ')#rfind procura o ultimo espaço da string
print(posicao)
print('Seu ultimo nome é: {}'.format(nome[posicao+1:].title()))