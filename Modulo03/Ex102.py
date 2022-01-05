def fatorial(n, show):
    """
    Doc String:
        Calcula o fatorial de um numero
    """
    f = 1
    for c in range(n,0,-1):

        if show == True:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c

    return f


print(fatorial(5, show=True))