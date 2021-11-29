char = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while char != 'M' and char != 'F':
    char = str(input('Dados invalidos. Por favor, informe seu sexo corretamente [M/F]: ')).strip().upper()[0]
print(f'Sexo {char} salvo com sucesso!!!')