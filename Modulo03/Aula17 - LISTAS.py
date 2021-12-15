num = [2,5,9,1]

print('Lista:' , num)


num.append(4) #adicionando valores a lista
print('\nAdicionando valores:', num)

num.sort()
print('\nLista organizada de forma crescente:', num) #Organuza lista de forma crescente

num.sort(reverse=True) #Organiza lista de forma decrecente
print('\nLista organizada de forma decrecente:',num)

print('\nConta a quantidade de elementos da lista:', len(num))

num.insert(2,0) #Irá inserir o numero '0' na posição '2' da lista, mas o antigo valor que estava na posição 2 são será deletado, ele será recolocado para a proxima posição, e assim sucetivamente.
print('\nInsere valor na posição especifica sem deletar o antigo:', num)

num.pop() # Apaga ultimo valor da lista
print('\nApaga ultimo valor da lista:', num)

num.remove(2) #elimina o primeiro elemente especificado que for encontrado na lista
print('\nElimina o primeiro elemente especificado que for encontrado na lista:', num)


#Estrutura para verificarr se o valor existe na lista para apagalo
if 4 in num:
    num.remove(4)
    print('\nValor 4 apagado da lista: ', num)
else:
    print('\nNão existe valor 4 na lista:', num)

#Estrutura de for para verificar chave e valores da lista
num.append(8)
num.append(2)
num.append(9)
print('\nEstutura for com a lista:', num)
for c, v in enumerate(num):
    print(f'Na posição {c}, encontrei o valor = {v}!')
print('Cheguei ao final da lista.')

#Quando se igualar duas lista, é importante lembrar que o python cria uma ligação entre elas, tudo que for alterado em uma lista se replicara na outra. Exemplo:
print()
a = [2,8,1,4]
b = a
b[2] = 7 #Essa alteração correra na lista 'a' também, isso devido a ligação feita com pelo próprio Python
print(f'Lista A = {a}')
print(f'Lista B = {b}')

print()
#Para criar uma copia da lista, sem que exista uma ligação devemos usar a seguinte sintaxe
b = a[:] #Pega todos os valores de 'a' e joga em 'b', sem criar uma ligação.
b[2] = 10
print(f'Lista A = {a}')
print(f'Lista B = {b}')