contador= 0
maior= 0
menor= 0
soma= 0

while True:
    num = int(input("Digite um número: "))
    contador+= 1
    soma += num
    if contador == 1:
        menor = num
        maior = num
    else:
        if num < menor:
           menor = num
        if num > maior:
           maior = num
    while True:
        continuar= str(input("Deseja continuar? [S/N] ")).upper()
        if continuar in ["N","S"]:
            break
        else:
            print("Digite apenas S ou N")
    if continuar == "N":
            break

media = soma / contador
print(f"Média {media:.2f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")









