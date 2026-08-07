def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31m Erro! Digite um número inteiro válido.\033[m')



#Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')




