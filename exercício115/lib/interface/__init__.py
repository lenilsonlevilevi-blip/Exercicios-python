def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31m Erro! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def linha(tam=30):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt:^30}')
    print(linha())


def menu(lista):
    cabeçalho('\033[34;40mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[32m {c} \33[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mSua opção: \033[m')
    return opc
