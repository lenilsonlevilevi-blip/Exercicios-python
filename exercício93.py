campeonato = {}
aproveitamento = []
tot_gols = 0

nome = str(input("Nome: "))
campeonato['nome'] = nome
partidas = int(input(f"Quantas partidas {nome} jogou? "))


for i in range(partidas):
    gols= int(input((f"Quantos gols na partida {i+1}? ")))
    tot_gols += gols
    aproveitamento.append(gols)

campeonato['gols'] = aproveitamento
campeonato['total de gols'] = tot_gols

print(campeonato)

for k, v in campeonato.items():
    print(f"{k} tem o valor {v}")

print()

print(f"o jogador {nome} jogou {partidas} partidas.")
for i, v in enumerate(aproveitamento):
    print(f"na partida {i+1}, fez {v} gols.")

