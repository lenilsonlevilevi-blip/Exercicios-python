from random import randint
from time import sleep
numeros = []

def sorteia():
    print(f'Sorteado 5 valores da lista', end=' ')
    for c in range(5):
        num = randint(1, 10)
        numeros.append(num)
        sleep(0.5)
        print(f'{num} ', end='')

def somapar():
    par = 0
    for n in numeros:
        if n % 2 == 0:
         par += n
    print(f'\nA soma dos valores pares {numeros} é {par}.')




sorteia()
somapar()



