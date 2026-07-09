frase = input("Digite uma frase: ").upper().strip()
junto = ""
inverso = junto[::-1]
print(f"{junto} {inverso}")
if inverso == junto:
    print("Essa frase é um PALÍDROMO!")
else:
    print("Essa frase não é um PALÍDROMO!")
