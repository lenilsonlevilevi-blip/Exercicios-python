sexo = ""
while sexo != "F" and sexo != "M":
    sexo = str(input("Qual seu sexo? [M/F]: ")).upper()
    if sexo != "M"and sexo != "F":
        print("Digite uma opção válida")

print("Programa encerrado")