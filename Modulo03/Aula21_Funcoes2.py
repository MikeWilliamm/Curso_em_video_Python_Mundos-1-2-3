print('-='*30)
print('DOC STRINGS: \n')
#doc strings
def contador(i,f,p):
    #isso é um doc string, será exibido quando a função for chamada no help
    """ 
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passo da contagem
    """
    while i <= f:
        print(i, end='..')
        i += p

contador(0,10,2)

help(contador)

print('-='*30)
print('PARAMETROS OPCIONAIS: \n')
#parametros opcionais

def soma(a,b,c=0): #C possuio o valor opicional 0, caso a função não receba nenhum parametro para 'c', então ele valera 0
                   #É possivel  definicar todos os parametros com valores opcionais.
    s = a + b +c
    print(f'a soma de {a} + {b} + {c} é igual a {s}')

soma(5,2,3)
soma(5,2)

print('-='*30)
print('ESCOPO DE VARIAVEIS: \n')
#escopo de variaveis

def teste():
    x = 8
    print(f'Na função teste n vale {n}!')
    print(f'Na função teste x vale {x}!')
#programa principal
n = 2 
#mesmo 'n' não estando dentro da função teste, ele podera ser acessado de dentro da função, isso devido ele estar
#no escopo global
print(f'No programa principal n vale {n}!')
teste()
#print(f'No programa principal x vale {x}!') = retornara ERRO, como a variavel x está DECLARADO dentro da função, ela 
# é uma variavel local que só funcionara dentro da função;

print('-='*30)
print('Escopo global e local: \n')
#Escopo global e local

#No momento em que uma variavel é passada como parametro para uma função, é feito uma copia da variavel original para a variavel da função, a variavel
#da função não tem ligação com a variavel original, assim não será alterado nada na variavel original.

#variaveis local = variaveis declaradas dentro de uma função, ou seja escopo local.
#variaveis globais = variaveis declaradas no programa principal.

def soma2(b):
    #a = 1 Se uma variavel for declarada de forma local dentro de uma função, e ela já existir no escopo global, então todas altereçoes seram feitas na variavel local,
    #não aterando a variavel do escopo global, para isso correr não pode-se fazer a declaração global a baixo

    global a
    #para trabalharmos na variavel global dentro de uma função, é necessário utilizar o global nome_variavel ex:
    print(f'Varial global "a" da que foi passada como parametro para b na funcção soma e é trazida como variavel global vale {a}')
    
    b += 2 #variavel local que foi passada como copia da global
    print(f'Variavel local da "b" da função vale {b}')
    

    



#programa principal
a = 5 #variavel global
soma2(a)

print(a)

print('-='*30)
print('Retorno de valor: \n')
#Retorno de valores
def somar3(a = 0, b = 0, c = 0): #parametros opcionais
    s = a+b+c

    return s #retorna o valor da soma para a variavel que chamou a função


r1 = somar3(1,2,2)
r2 = somar3(1,7)
r3 = somar3(4)

print(f'As somas valem {r1}, {r2} e {r3}')