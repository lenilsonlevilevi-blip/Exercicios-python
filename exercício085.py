pares = []
impares = []

lista = [pares, impares]
for c in range(1,8):
    n = int(input(f'Digite o {c}° valor: '))

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort()

print(f"Números pares digitados {lista[0]}")
print(f"Números ímpares digitados {lista[1]}")