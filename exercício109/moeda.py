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
