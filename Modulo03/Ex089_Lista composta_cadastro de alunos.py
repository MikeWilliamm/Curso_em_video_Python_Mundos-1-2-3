boletim = []
aux = []
contador = 0
while True:
    aux.append(contador)
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    boletim.append(aux[:])
    aux.clear()

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp != 'N' and resp != 'S':
        print('Digito ERRADO!!!')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    if resp == 'N':
        break

    contador += 1

print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)

for p in boletim:
    print(f'{p[0]:<4}{p[1]:<10}{(p[2] + p[3]) /2:>8.1f}')

print('-'*50)
while True:
    mostrar = int(input('Mostrar a nota de qual aluno ? [ID] '))
    contador = verifica = 0

    for p in boletim:
        if p[0] == mostrar:
            print(f'Notas de {p[1]} são {p[2]} e {p[3]}')
            verifica = 1
        elif contador == len(boletim)-1 and verifica == 0:
            print('ID INVALIDO!!!')
        contador += 1 
    
    

    resp = str(input('\nDeseja mostrar a nota de um aluno novamente? [S/N] ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('\nDigito ERRADO!!!')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    print()
    
    if resp == 'N':
        break

print('Programa Finalizado')