num = []
while True:
    n = int(input("Digite um número: "))
    num.append(n)
    continuar = input("Deseja continuar? [S/N]").strip().upper()
    while continuar not in "SN":
        continuar = input("Resposta Inválida. Deseja continuar? [S/N]").strip().upper()
    if continuar == "N":
        break

num.sort(reverse=True)
print(f"\nForam digitados {len(num)} números")
print(f"A lista digitada foi: {num}")

if 5 in num:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista.")




