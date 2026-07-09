lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    c = input("Deseja continuar? [S/N]").upper().strip()
    if c == "N":
        break

print("-="*30)
print(f"Lista completa: {lista}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
