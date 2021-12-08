brasileirao = ('Corinthians','Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia',  'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')


print(f'\nLista de times do brasileirão: \n{brasileirao}')
print(f'\nOs 5 primeiros colocados do brasileirão são: \n{brasileirao[:5]}')
print(f'\nOs 4 ultimos colocados do brasileirão são: \n{brasileirao[-4:]}')
print(f'\nTimes em ordem alfaberica: \n{sorted(brasileirao)}')

#Encontrar index
for i in range(len(brasileirao)):
    if brasileirao[i] == 'Chapecoense':
        print(f'\no {brasileirao[i]} está na posição {i+1} de um total de {len(brasileirao)+1} posições.')

#Forma simplificada para encontrar
print(f'\nO Chapecoense está na {brasileirao.index("Chapecoense")+1} posição')
