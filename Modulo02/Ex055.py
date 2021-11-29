maior = 0 
menor = 0

for i in range(1,5):
    peso = float(input('Digite o peso {}: '.format(i)))
    
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'Menor peso: {menor}\nMaior peso: {maior}')























# maior =0
# menor = 0

# for i in range(1,5):
#     peso = float(input(f'Digite o peso da {i} pessoa: '))
    
#     if i == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         elif peso < menor:
#             menor = peso

# print(f'Menor peso: {menor}\nMaior peso: {maior}')