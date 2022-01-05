

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano 
    if idade < 16:
        return (f'Com {idade} anos: NÃO VOTA!')
    elif idade >= 16 and idade < 18 or idade >= 65:
        return(f'Com {idade} anos: VOTO OPCIONAL!')
    elif idade >= 18:
        return(f'Com {idade} anos: VOTO OBRIGATÓRIO!')

ano = int(input('Em que ano você nasceu? '))        
print(voto(ano))