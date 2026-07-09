from random import randint
print('=-=' * 10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print('=-=' * 10)
vitorias = 0

while True:
    maquina = randint(1, 10)
    jogador = int(input("Digite um valor: "))
    jdr2 = str(input("Par ou Ímpar [P/I]: ")).upper()

    soma = maquina + jogador

    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    print(f"Você escolheu {jogador} e o Computador {maquina} total = {soma}", end=" ")
    print("DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR")

    if resultado == jdr2:
        print("Você ganhou!")
        vitorias += 1
    else:
        print("Você perdeu! Tente novamente.")
        break
print(f"\nGAME OVER! Você venceu {vitorias} vezes seguidas.")








