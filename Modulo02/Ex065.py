resp = 'S'
soma = 0
contador = 0
maior = 0
menor = 0
const = 0
while resp == 'S':
    const = int(input('Digite um numero: '))
    soma += const
    contador += 1

    if contador == 1:
        maior = const
        menor = const
    else:
        if maior < const:
            maior = const
        elif menor >=  const:
            menor = const

    resp = str(input('Deseja continuar (S/N): ')).upper().strip()

print(f'Você digitou {contador} numeros e a média foi {soma/contador}\nO maior numero é {maior} e o menor numero é o {menor}')
