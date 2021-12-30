#No python a passagem de parametros é por referencia, diferente de outras longuagens que é por valor.

def mensagem(txt):
    print('-'*30)   
    print(txt)
    print('-'*30)

mensagem('CURSO EM VIDEO')
mensagem('PYTHON')
mensagem( 'Mike')

def soma(a,b):

    s = a + b
    print(f'{a} + {b} = {s}' )

a = 5
b = 2
soma(a, b)
soma(1,2) #parabemtros passados em ordem.
soma(b = 1, a = 4) #especificando aprametros.

print('-'*30)
def contador(*num): #recebe uma tupla com valores infinitos, utilizar quando não se sabe a quantidade de valores que a função irá receber
    for i in num:
        print(f'{i}', end = '')
    print(' - FIM')

contador(8,6,2,4)
contador(6,5)
contador(8,4,1)

print('-'*30)
def dobra(lst):
    pos = 0 
    print(lst)
    for i in lst:
        i = i*2
        print(i, end= ' ')
        


lista_teste = [2,1,5,4,8]
dobra(lista_teste) #tudo que for feito na lista dentro da função, irá afera a lista original fora da função
print('\n')
print('-'*30)

def soma2(*valores): #recebendo diversos 'N' VALORES EMPACOTADOS
    s = 0
    for num in valores:
        s+= num
    print(f'Somando {valores} temos {s}')
soma2(2,4,3,5,1,0)