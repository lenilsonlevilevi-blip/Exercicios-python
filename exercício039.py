#Alistamento militar
from datetime import date
ano_atual= (date.today().year)
ano_nascimento= int(input("Digite o ano de nascimento: "))
idade= (ano_atual - ano_nascimento)


if idade < 18:
    print(f"Ainda não está na hora. Faltam {18 - idade} anos.")
elif idade == 18:
    print("Está na hora de se alistar")
elif idade > 18:
    print(f"Já passou do prazo do alistamento. Você está {idade - 18} anos atrasado.")
