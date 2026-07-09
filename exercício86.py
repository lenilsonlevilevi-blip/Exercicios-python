# Cria uma matriz 3x3 preenchida inicialmente com zeros
matriz = [[0,0,0],[0,0,0],[0,0,0]]

# Percorre as linhas da matriz
for l in range(0,3):
    # Percorre as colunas da matriz
    for c in range(0,3):

        # Pede um valor ao usuário e armazena
        # na posição correspondente da matriz
        matriz[l][c] = int(input(f"Digite um valor para [{l} e {c}]:"))

# Mostra uma linha decorativa
print("-=" * 20)

# Percorre novamente as linhas
for l in range(0,3):

    # Percorre novamente as colunas
    for c in range(0,3):

        # Mostra cada valor formatado
        # :^4 = centraliza o número em 4 espaços
        # end=" " evita quebrar linha automaticamente
        print(f"[{matriz[l][c]:^4}]", end=" ")

    # Quebra a linha após terminar cada linha da matriz
    print()






