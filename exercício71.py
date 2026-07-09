print("==" * 20)
print("     BANCO CÉU    ")
print("==" * 20)
valor = int(input("Quanto você quer sacar: "))

divisao = valor // 50
resto = valor % 50
divisao2 = resto // 20
resto2 = resto % 20

divisao3 = resto2 // 10
resto3 = resto2 % 10

divisao4 = resto3 // 1
resto4 = resto3 % 1

print(f"total de {divisao} cédulas de R$ 50,00")
print(f"total de {divisao2} cédulas de R$ 20,00")
print(f"total de {divisao3} cédulas de R$ 10,00")
print(f"Total de {divisao4} moedas de R$ 1,00")
print("==" * 20)
print("Volte sempre ao BANCO CÉU! Tenha um bom dia!")
print("==" * 20)



