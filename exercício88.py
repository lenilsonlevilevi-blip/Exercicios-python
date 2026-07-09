from random import randint  # Importa a função randint para gerar números aleatórios
lista = []  # Lista que irá armazenar todos os jogos sorteados

# Pergunta quantos jogos o usuário deseja gerar
quant = int(input("Quantos jogos você quer que eu sorteie? "))

# Repete a criação dos jogos de acordo com a quantidade informada
for i in range(quant):

    jogos = []  # Cria uma lista vazia para armazenar os 6 números do jogo atual

    # Continua sorteando enquanto o jogo tiver menos de 6 números
    while len(jogos) < 6:

        # Sorteia um número entre 1 e 60
        numero = randint(1, 60)

        # Verifica se o número ainda não existe no jogo
        if numero not in jogos:

            # Adiciona o número ao jogo
            jogos.append(numero)

    # Organiza os números em ordem crescente
    jogos.sort()

    # Adiciona o jogo completo à lista principal
    lista.append(jogos)

# Percorre todos os jogos armazenados na lista
for i, jogos in enumerate(lista):

    # Exibe o número do jogo e seus números sorteados
    print(f"Jogo {i + 1}: {jogos}")















