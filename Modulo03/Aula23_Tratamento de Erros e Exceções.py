try: 
    a = int(input('Número: '))
    b = int(input('Número: '))
    r = a/b
    
except (ValueError, TypeError) as erro:
    print( f'ERRO de valor: {erro}')
    print('Tivemos um problema com tipo de valor que você digitou!')
except ZeroDivisionError as erro:
    print(f'ERRO de divisão: {erro}')
    print('Impossivel dividar valor por 0')
except KeyboardInterrupt:
    print('\nO usuario preferiu não informar os dados!')
except Exception as erro:
    print(f'ERRO GENÉRICO: {erro}')
else: #Só entrara no else se o 'try' der certo.
    print(f'{a}/{b} = {r:.2f}')
finally: #Irá executar dando certo o 'try' ou não.
    print('Volte sempre! Muito obrigado!')