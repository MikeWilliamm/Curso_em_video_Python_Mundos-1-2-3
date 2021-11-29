soma = mil = barato = cout = nomeBarato = 0
print('-'*20 + ' LOJA SUPER BATARÃO ' + '-'*20)

while True:
    nomeProduto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: '))
    
    cout +=1
    soma += valor

    if valor > 1000:
        mil +=1
    
    if cout == 1:
        barato = valor
        nomeBarato = nomeProduto 
    else:
        if barato > valor:
            barato = valor
            nomeBarato = nomeProduto 
    resp = str(input('Deseja continuar? [S/N]: ')).strip()[0]

    while resp.upper() not in 'SN':
        print('\nDigito invalido!')
        resp = str(input('Deseja continuar? [S/N]: '))
    
    if resp.upper() == 'N':
        break

print(f'''\nO Total da compra foi {round(soma, 3)}
Temos {mil} produtos custando mais que R$1000.00
O produto mais barato é {nomeBarato} e custa {barato}''')