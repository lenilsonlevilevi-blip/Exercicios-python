from time import sleep
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

while True:
    print("\n[ 1 ]somar")
    print("[ 2 ]multiplicar")
    print("[ 3 ]maior")
    print("[ 4 ]novos números")
    print("[ 5 ]sair do programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = n1 + n2
        print(f"A soma dos números é {soma}")

    elif opcao == 2:
        multiplicar = n1 * n2
        print(f"A multiplicação dos números é {multiplicar}")

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior número digitado é {maior}")

    elif opcao == 4:
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
        continue

    elif opcao == 5:
        print("Saindo do programa...")
        sleep(3)
        print("Programa finalizado com sucesso!")
        break
    else:
        print("Opção invalida!")
        continue

    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
