matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0
soma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz [l][c]=int(input(f"Digite um valor para [{l} e {c}]:"))
        if matriz[l][c] % 2 == 0:
            pares += matriz [l][c]
print()
print("     RESULTADO DA MATRIZ     ")
print("-="*20)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

print("-="*20)
print(f"A soma dos valores pares é {pares}")
for l in range(0,3):
    soma += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {soma}")
print(f'O maior valor da segunda linha é {max(matriz[1])}')





