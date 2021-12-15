palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis'
            'estudar', 'praticar','trabalhar', 'mercado', 'programador', 'futuro')
    
print(palavras)

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')