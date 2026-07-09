# cria uma lista vazia
valores = []

# repete 5 vezes
for c in range(0,5):

    # pede um número ao usuário
    n = int(input(f"Digite um valor: "))

    # SE for o primeiro número
    # OU se o número digitado for maior que o último da lista
    if c == 0 or n > valores[-1]:

        # adiciona no final da lista
        valores.append(n)

        print("adicionado ao final da lista.")

    else:

        # variável para controlar a posição
        pos = 0

        # enquanto a posição for menor que o tamanho da lista
        while pos < len(valores):

            # se o número for menor ou igual ao valor daquela posição
            if n <= valores[pos]:

                # insere o número naquela posição
                valores.insert(pos, n)

                print(f"o valor {n} foi adicionado na posição {pos}.")

                # encerra o while
                break

            # vai para a próxima posição
            pos += 1

# mostra a lista final
print(valores)

