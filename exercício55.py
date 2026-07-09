# Cria duas variáveis para guardar o maior e o menor peso
maior = 0
menor = 0

# Loop que vai repetir 5 vezes (de 1 até 5)
for i in range(1, 6):

    # Pede para o usuário digitar um peso
    # f-string mostra qual número está sendo digitado (1°, 2°, etc.)
    peso = float(input(f"Informe o {i}° peso: "))

    # Se for a primeira vez do loop (i = 1)
    if i == 1:
        # O primeiro peso vira a base de comparação
        # Nesse momento ele é ao mesmo tempo o maior e o menor
        maior = peso
        menor = peso

    else:
        # Se o peso atual for maior que o maior armazenado
        if peso > maior:
            # Atualiza o maior
            maior = peso

        # Se o peso atual for menor que o menor armazenado
        if peso < menor:
            # Atualiza o menor
            menor = peso

# Depois do loop terminar, mostra os resultados finais
print(f"O maior peso lido foi de {maior}Kg")
print(f"O menor peso lido foi de {menor}Kg")



