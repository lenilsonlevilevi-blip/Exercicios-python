jogadores = []

while True:
    jogador = {}
    aproveitamentos = []
    total_gols = 0

    jogador['Nome'] = str(input('Nome: '))
    partidas = int(input('quantas partidas? '))

    for p in range(partidas):
        gols = int(input(f'Quantos gols na partida {p+1}? '))
        total_gols += gols
        aproveitamentos.append(gols)

    jogador['gols'] = aproveitamentos
    jogador['total de gols'] = total_gols

    jogadores.append(jogador.copy())

    resp = input("Deseja continuar? [S/N]?").strip().upper()[0]
    print('-'*30)
    if resp == 'N':
        break

for cod, j in enumerate(jogadores):
    print(f"{cod:>3} Cod nome {j['Nome']:<5} gols {j['gols']} total de gols {j['total de gols']:>3} ")


while True:
    dados = int(input("Quer mostrar dados de qual jogador? [999] Pra parar "))
    encontrou = False

    if dados == 999:
        print('>>>VOLTE SEMPRE<<<')
        break


    for cod, j in enumerate(jogadores):
        if dados == cod:
            print(f"{j['Nome']} jogou {partidas} partidas.")
            for i, v in enumerate(j['gols']):
                print(f'    =>Na partida {i+1} fez {v} gols.')

            encontrou = True

    if not encontrou:
        print("Número inválido")







