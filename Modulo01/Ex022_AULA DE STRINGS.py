from pandas.io.parsers import count_empty_vals


frase = str(input('Digiete uma frase: '))
print('\n')

print('Conta quantidade de letras ''o'' digitadas: ')
conta = frase.count('o')
print(conta)

print('-' *20)
print('Conta a quantidade de letras o na frase entre as posições 0 até 2 da string')
conta2 = frase.count('o', 0, 2) #no fatiamento o ultimo valor é ignorado, ou seja só será analisado de 0 a 1
print(conta2)

print('-' *20)
print ('Produta coisas dentro da strign, procurar a plavra ''go'': ')
conta3 = frase.find('go')#se o retorno for -1 é porque não existe a palavra procurada
print(conta3)

print('-' *20)
print('Retorna true ou false para a palavra pesquisada: ')
conta4 = 'amigo' in frase
print(conta4)

print('-' *20)
print('Troca a palavra desejada por outra: ')
conta5 = frase.replace('amigo', 'diana')
print(conta5)

print('-' *20)
print('Deixa a frase maiscula: ')
conta6 = frase.upper()
print(conta6)

print('-' *20)
print('Deixa a frase minuscula: ')
conta6 = frase.lower()
print(conta6)

print('-' *20)
print('Primeira letra maisucula e o restante minuscula: ')
conta6 = frase.capitalize()
print(conta6)

print('-' *20)
print('Primeira letra e toda palavra depois de uma espaço ficam com a primeira letra maiuscula:')
conta6 = frase.title()
print(conta6)

print('-' *20)
print('Remove espaços inuteis do começo e do final da string: ')
conta6 = frase.strip()
print(conta6)

print('-' *20)
print('Remove espaços inuteis do lado direito(final) da string: ')
conta6 = frase.rstrip()
print(conta6)

print('-' *20)
print('Remove espaços inuteis do lado esquerdp(inicio) da string: ')
conta6 = frase.lstrip()
print(conta6)

print('-' *20)
print('Cada palavra que é separada por um espaço é transformada em uma lista diferente: ')
conta7 = frase.split()
print(conta7)

print('-' *20)
print('realiza a junção da string splitada anteriormente: ')
conta7 = '-'.join(conta7)
print(conta7)

print('-' *20)
print('Fatiando da segunda até a quarta letra: ')

print(frase[1:5])

print('-' *20)
print('Fatiando da segunda letra ate o final: ')

print(frase[1:])

print('-' *20)
print('printando pulando dus caracteres por vez: ')

print(frase[::2])#pode fatiar coloca o periodo de letras deseja igual anteriormente

print('-' *20)
print('printando um texto grande: ')

print('''afassssssssssssssssssssssssssssssssssssssssssssssssssssss
sssssssssssssssssssssssssssssssssssssssssssssssss
ssssssssssssssssssssssssssssssssssssssss ''')

print('-' *20)
print('Verificando o tamanho total da string com espaços somando também: ')

print(len(frase))

print('-' *20)
print('splitando e printando apenas primeira palavra da string: ')
dividido = frase.split()
print(dividido[0])