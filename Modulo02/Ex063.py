print('-'*20 + ' Sequencia de FIOBONACI ' + '-'*20)

qtd = int(input('Quantos termos quer somar? '))
i = 1
t1 = 0
t2 = 1
t3 = 0

print(t1, '-> ', t2, '-> ', end = '')
while i < qtd-1:
    t3 = t1 + t2
    print(t3, '-> ', end = '')
    t1 = t2
    t2 = t3
    i+=1

print('FIM')
    

