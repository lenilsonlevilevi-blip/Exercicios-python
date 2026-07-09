#Simulador de financiamento de Imóvel
casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salário: "))
anos = int(input("Em quantos anos vai pagar? "))

valor_mensal = casa / (anos * 12)
limite = salario * 0.3
print(f"Prestação mensal: R$ {valor_mensal:.2f}")

if valor_mensal > limite:
    print("Empréstimo REPROVADO!")
else:
    print("Empréstimo APROVADO!")
