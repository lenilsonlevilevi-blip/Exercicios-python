from datetime import date  # Importa a função para pegar a data atual

ano_atual = date.today().year  # Pega o ano atual automaticamente

totmenor = 0  # Contador de menores de idade
totmaior = 0  # Contador de maiores de idade

# Laço que vai repetir 7 vezes (para 7 pessoas)
for c in range(1,8):
    nascimento = int(input(f"Em que ano a {c}° pessoa nasceu: "))  # Pede o ano de nascimento
    # Calcula a idade e verifica se é menor ou maior de 21 anos
    if ano_atual - nascimento < 21:
        totmenor += 1  # Soma +1 no contador de menores
    else:
        totmaior += 1  # Soma +1 no contador de maiores

# Mostra o resultado final
print("\nResultado final")
print(f"Ao todo tivemos {totmenor} Menores de idade. ")  # Mostra quantos são menores
print(f"É também {totmaior} Maiores de idade. ")  # Mostra quantos são maiores



