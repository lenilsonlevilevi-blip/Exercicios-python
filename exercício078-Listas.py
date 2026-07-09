numeros= []
for p in range(5):
    numeros.append(int(input(f"Digite um número para a posição {p}: ")))
print("-=" * 20)
print(f"Você digitou os números {numeros}")

maior= max(numeros)
menor= min(numeros)

print(f"O maior número digitado foi: {maior} nas posições: ",end=" ")
for p, n in enumerate(numeros):
    if n == maior:
        print(f"{p} ", end=" ")

print(f"\nO menor número digitado foi: {menor} nas posições: ", end=" ")
for p, n in enumerate(numeros):
    if n == min(numeros):
        print(f"{p} ", end=" ")


