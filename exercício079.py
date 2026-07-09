valores = []
while True:
    n = (int(input("Digite um valor: ")))
    if n in valores:
        print("Valor duplicado. Não vou adicionar.")
    else:
        valores.append(n)
        print("Valor adicionado com sucesso.")

    continuar = input("Deseja continuar? [S/N] ").upper()
    if continuar == "N":
        break

valores.sort()
print("-=" * 30)
print(f"Você digitou os valores: {valores}")





