# Inicialização das variáveis
total_gasto = 0        # Vai acumular a soma de todos os preços
mais_de_mil = 0        # Conta quantos produtos custam mais de 1000
menor_preco = 0        # Guarda o menor preço encontrado
produto_mais_barato = " "  # Guarda o nome do produto mais barato
contador = 0           # Conta quantos produtos foram digitados

print("-=-=-=-=-=-=-=-=-=-=-=-=-")
print("       LOJA DO LEVI      ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-")
# Loop principal (repete até o usuário decidir parar)
while True:

    # Entrada de dados
    produto = str(input("Qual o nome do produto? "))
    preco = float(input("Preço R$:  "))

    # Incrementa o contador (indica quantos produtos já foram cadastrados)
    contador += 1

    # Se for o primeiro produto
    if contador == 1:
        # Não dá pra comparar ainda, então ele vira o mais barato por padrão
        menor_preco = preco
        produto_mais_barato = produto
    else:
        # Para os próximos produtos, faz a comparação
        if preco < menor_preco:
            # Se encontrar um preço menor, atualiza
            menor_preco = preco
            produto_mais_barato = produto

    # Verifica se o produto custa mais de 1000
    if preco > 1000:
        mais_de_mil += 1  # Incrementa o contador

    # Soma o preço ao total gasto
    total_gasto += preco

    # Pergunta se o usuário quer continuar
    continuar = str(input("Deseja continuar? [S/N] ")).upper()

    # Se a resposta for "N", encerra o loop
    if continuar == "N":
        break
    print("-=-=-=-=-=-=-=-=-=-=-=-=-")


# Exibição dos resultados
print("-=" * 20)
print(f"Produto mais barato: {produto_mais_barato}")  # Mostra o nome do mais barato
print(f"Total gasto: {total_gasto}")                 # Mostra o total gasto
print(f"{mais_de_mil} produtos custam mais de R$ 1000.00")  # Mostra quantos > 1000