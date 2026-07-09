n = int(input("Digite um número: "))
fatorial = 1
contador = n

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {n} é {fatorial}")