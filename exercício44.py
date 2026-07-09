#calcula o preço do produto baseado na forma de pagamento
produto = float(input("Preço do produto:R$ "))
print("""QUAL A FORMA DE PAGAMENTO?
[1] CARTÃO/CHEQUE
[2] Á VISTA NO CARTÃO
[3] 2X NO CARTÃO 
[4] 3X OU MAIS NO CARTÃO """)

pgm = str(input("Qual a opção desejada? "))

valor_final = produto
if pgm == "1":
    valor_final = produto * 0.90
    print(f"O valor final a ser pago é:R${valor_final:.2f}")
elif pgm == "2":
    valor_final = produto * 0.95
    print(f"O valor final a ser pago é:R${valor_final:.2f}")
elif pgm == "3":
    valor_final = produto / 2
    print(f"O valor final a ser pago é:2x de R${valor_final:.2f}")
elif pgm == "4":
    parcela = int(input("Em Quantas parcelas?"))
    if parcela < 3:
        print("Para essa opção, mínimo de 3 parcelas.")
    else:
        total = produto * 1.20
        valor_final = total / parcela
        print(f"O valor do produto com juros é: R$ {total:.2f}")
        print(f"Fica {parcela}x de R$ {valor_final:.2f}")
else:
    print("opção invalida!")


