from time import sleep

def contador(i, f , p):
    if p == 0:
       p = 1
    if p < 0:
       p = -p

    if i < f:
        for c in range(i,f+1,p):
            print(f'{c}', end=' ')
            sleep(0.5)

    elif i > f:
        for c in range(i,f-1,-p):
            print(f'{c}', end=' ')
            sleep(0.5)

print("-=" * 24)
print("Contagem de 1 até 10 de 1 e 1")
contador(1, 10, 1)
print()

print("-="*24)
print("Contagem de 10 até 0 de 2 em 2")
contador(10, 0, 2)

print()
print("-=" * 24)
print("Agora é a sua vez de personalizar a contagem")
i= int(input("Início: "))
f= int(input("Fim: "))
p= int(input("Passo: "))
print(f"Contagem de {i} até {f} em {p} em {p}")
contador(i, f, p,)
print("FIM")





