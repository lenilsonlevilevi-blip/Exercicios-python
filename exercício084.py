# lista principal que guarda nome e peso de cada pessoa
cadastro = []

# variáveis para armazenar maior e menor peso
maior = menor = 0

# laço principal do programa
while True:

    # recebe o nome da pessoa
    nome = str(input('Digite o seu Nome:  '))

    # recebe o peso da pessoa
    peso = float(input('Digite o seu Peso: '))

    # adiciona nome e peso dentro da lista cadastro
    # exemplo: ["Levi", 80]
    cadastro.append([nome, peso])

    # verifica se é o primeiro cadastro
    if len(cadastro) == 1:

        # o primeiro peso será o maior e o menor inicialmente
        maior = menor = peso

    else:

        # verifica se o peso atual é maior que o maior peso salvo
        if peso > maior:
            maior = peso

        # verifica se o peso atual é menor que o menor peso salvo
        if peso < menor:
            menor = peso

    # pergunta se deseja continuar
    resp = str(input('Deseja continuar? [S/N] '))

    # encerra o programa caso a resposta seja N
    if resp in 'Nn':
        break

# linha decorativa
print("-=" * 40)

# quantidade total de pessoas cadastradas
print(f"Ao todo, foram cadastradas {len(cadastro)} pessoas")

# mostra o maior peso encontrado
print(f"O maior peso foi de {maior}kg. Peso de", end=" ")

# percorre toda a lista cadastro
for p in cadastro:

    # verifica quem possui o maior peso
    if p[1] == maior:

        # p[0] = nome da pessoa
        print(f"{p[0]},", end=" ")

# mostra o menor peso encontrado
print(f"\nO menor peso foi de {menor}kg. Peso de", end=" ")

# percorre novamente a lista cadastro
for p in cadastro:

    # verifica quem possui o menor peso
    if p[1] == menor:

        # mostra o nome da pessoa
        print(f"{p[0]},", end=" ")
