expressao = str(input('Digite uma expressao: ')).strip()
pilha = []

#(a*b)-)c(=12
#(a*b)(a(4+3)*2)(c)
for i in expressao:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua empressão é Valida!')
else: 
    print('Sua expressão é errada!')