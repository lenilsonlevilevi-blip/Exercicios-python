soma = 0
mais_velho_nome = ""
mais_velho_idade = 0
meninas_20= 0

for i in range(1,5):
    print(f"-------{i}°PESSOA--------")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("SEXO [M/F]: ").upper()

    soma+= idade

    if sexo == "M":
        if idade > mais_velho_idade:
            mais_velho_nome = nome
            mais_velho_idade = idade
    if sexo == "F":
        if idade < 20:
            meninas_20 += 1

media = soma / 4
print(f"{meninas_20} mulheres com menos de 20 anos")
print(f"a média das idades é {media} anos")
print(f"O homem mais velho é {mais_velho_nome} com {mais_velho_idade} anos")
