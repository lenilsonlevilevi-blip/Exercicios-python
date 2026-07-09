print("CADASTRE UMA PESSOA")
idade18= 0
homem= 0
mulher_20= 0
while True:
    sexo = str(input("Digite o seu sexo [M/F]: ")).strip().upper()
    while sexo not in ["M","F"]:
        sexo = str(input("Valor inválido! Digite o seu sexo [M/F]: ")).strip().upper()
    idade = int(input("Digite sua idade: "))

    # CONTAGEM (vem antes do continuar)
    if idade > 18:
        idade18 += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher_20 += 1

    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    while continuar not in ["S","N"]:
        continuar = str(input("Valor inválido! Deseja continuar? [S/N]: ")).strip().upper()

    print("-=" * 15)
    if continuar == "N":
        break

print(f"Pessoas com mais de 18 anos: {idade18}")
print(f"Homens cadastrados: {homem}")
print(f"Mulheres com menos de 20 anos: {mulher_20}")




