alunos = {}

alunos ["nome"] = str(input("nome: "))
alunos ["média"] = float(input(f"Média de {alunos['nome']}: "))

print()

print(f"Nome é igual {alunos['nome']}")
print(f"Sua média é igual a {alunos['média']}")

if alunos["média"] >= 7:
    print("Situação é igual Aprovado")
else:
    print("Situação é igual Reprovado")


