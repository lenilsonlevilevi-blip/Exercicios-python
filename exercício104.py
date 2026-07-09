def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um número: '))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break

        else:
            print('Erro! Digite um número inteiro válido.')
    return valor

#Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')




