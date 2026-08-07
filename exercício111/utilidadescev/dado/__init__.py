def leiadinheiro():
    while True:
        try:
            p= float(input('Digite um valor: '))
            print(f'Você digitou o número {p}')
            break
        except ValueError:
            print('\33ERROR! Dite um valor válido\33')
