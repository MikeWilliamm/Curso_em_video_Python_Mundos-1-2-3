lista = []

for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))

print(f'\nVocê digitou os valores {lista}')

maior = 0
menor = 0
count = 0

for c, i in enumerate(lista):
    if count == 0:
        maior = i 
        menor = i
        count = 1
    else:
        if i >= maior:
            maior = i
        if i <= menor:
            menor = i

posicoes_maior = []
posicoes_menor = []

for i in range(0,len(lista)):
    if lista[i] == maior:
        posicoes_maior.append(i)
    if lista[i] == menor:
        posicoes_menor.append(i)

posicoes_maior = '... '.join(map(str, posicoes_maior)) # a função 'map' mapea todos os valores numerios da lista e transforma em string
posicoes_menor = '... '.join(map(str, posicoes_menor))
print(f'\nO Maior valor digitado foi {maior} nas posições {posicoes_maior}...')
print(f'O Menor valor digitado foi {menor} nas posições {posicoes_menor}...')