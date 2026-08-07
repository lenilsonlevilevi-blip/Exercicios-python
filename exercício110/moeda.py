def resumo(p, a=0, d=0):
    print('-'*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-'*30)

    print(f"{'preço analisado:':<20}R${p:.2f}")
    print(f'{'dobro do preço:':<20}{dobro(p,True)}')
    print(f'{'metade do preço:':<20}{metade(p,True)}')
    print(f'{f"{a}% de aumento:":<20}{aumentar(p,a, True)}')
    print(f'{f"{d}% de redução:":<20}{diminuir(p,d, True)}')

    print('-'*30)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def aumentar(n=0, taxa=0, p=False):
    res = n + (n * taxa / 100)
    if p == True:
        return moeda(res)
    else:
        return res

def diminuir(n=0,taxa=0,p=False):
    res = n - (n * taxa / 100)
    if p == True:
        return moeda(res)
    else:
        return res

def metade(n=0,p=False):
    if p == True:
        return moeda(n / 2)
    else:
        return n / 2

def dobro(n=0,p=False):
    if p == True:
        return moeda(n * 2)
    else:
        return n * 2
