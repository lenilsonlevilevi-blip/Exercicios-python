#converter para binário, octa e hexadecimal
num = int(input("Digite um número inteiro: "))

print("""ESCOLHA UMA DAS BASES PARA A CONVERSÃO   
[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL""")

opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    print(f"{num} convertido para binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para octal é {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para hexadecimal é {hex(num)[2:]}")
else:
    print("Opção inválida! tente novamente.")