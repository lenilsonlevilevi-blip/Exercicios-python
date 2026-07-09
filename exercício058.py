from random import randint
gerador = randint(0,10)
totjogador = 0
jogador = 0
while True:
    jogador = int(input("Digite um número: "))
    totjogador += 1
    if gerador == jogador:
        print("PARABÉNS! VOCÊ GANHOU!")
        break
    else:
        print("TENTE NOVAMENTE!")

print("O número correto era {}".format(gerador))
print("O jogador tentou {} vezes até acerta!".format(totjogador))