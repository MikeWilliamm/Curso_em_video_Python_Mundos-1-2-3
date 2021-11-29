nome = str(input('Digite seu nome: ')).strip()

print('Seu nome maiusculo é {}'.format(nome.upper()))
print('Seu nome minusculo é {}'.format(nome.lower()))
print('Seu nome tem o total de {} letras'.format(len(nome.strip().replace(' ', ''))))#Método replace
print('Seu nome tem o total de {} letras'.format(len(nome) - nome.count(' ')))#Método count - conta espaços
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} lentras'.format(dividido[0], len(dividido[0]))) #Método split
