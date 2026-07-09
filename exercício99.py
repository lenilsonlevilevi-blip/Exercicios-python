from time import sleep
def analisar(*num):
    print(f"Analisando os valores passados...")
    if len(num) == 0:
        maior = 0
    else:
        maior = max(num)
    for n in num:
        print(f'{n}', end=" ")
        sleep(0.5)
    print(f"\nforam informados {len(num)} valores ao todo ")
    print(f'O maior valor é {maior}')
    print("-="*24)


analisar(3,5,8,9,2)
analisar(15,8,9)
analisar(8,9,2)
analisar()