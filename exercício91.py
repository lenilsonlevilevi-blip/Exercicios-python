from random import randint
from time import sleep
jogadores = {}
print("Valores Sorteados:")
sleep(2)
for i in range(1,5):#i é a variável que guarda o número atual da repetição do for.

    jogadores[f"jogador{i}"] = randint(1,6)
    print(f"jogador{i:02} tirou {jogadores[f'jogador{i}']} no dado.")
    sleep(1)

print()
ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
print(" ==== Ranking dos jogadores ==== ")

for i, v in enumerate(ranking):
    print(f" {i+1}°lugar: {v[0]} {v[1]}")
    sleep(1)