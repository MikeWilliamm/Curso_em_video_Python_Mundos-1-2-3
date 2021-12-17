
valores = []
valor = 0
for i in range(0,5):

    valor = int(input('\nDigite um valor: '))

    if i == 0:
        valores.insert(i, valor)
        print('Adicionado o primeiro valor da lista!')
    else:
        for j in range(len(valores)):
            if valor <= valores[j]:
                valores.insert(j, valor)
                print(f'Adicionado na posição {j}')
                break
            
        if valor >= valores[-1]:
            valores.append(valor)
            print('Adicionado no final da lista!')    
print(valores)