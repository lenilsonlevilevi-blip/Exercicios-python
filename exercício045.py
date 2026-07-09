#jokenpõ
from random import choice
jogador = (input("Digite (PEDRA, PAPEL OU TESOURA): ")).lower().strip()
lista = ("pedra", "papel", "tesoura")

computador = choice(lista)

print(f"você escolheu: {jogador} ")
print(f"o computador escolheu: {computador}")

if jogador == computador:
    print("Ninguém ganhou!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")



