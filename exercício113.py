def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31m Erro! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31m Erro! Digite um número real válido.\033[m')
            continue
        else:
            return n

#programa principal
a = leiaint('Digite um inteiro: ')
b = leiafloat('Digite um real: ')
print(f'O Valor inteiro digitado foi {a} e o valor real {b}')

