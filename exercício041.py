#Lista de categoria para uma confederação de natação
from datetime import date
ano_atual= (date.today().year)
ano_nas= int(input("Digite o ano de nascimento: "))
idade= ano_atual - ano_nas
print(idade)

if idade <= 9:
    print("Sua categoria é MIRIM")
elif idade <= 14:
    print("Sua categoria é INFANTIL")
elif idade <= 19:
    print("Sua categoria é JUNIOR")
elif idade == 20:
    print("Sua categoria é SÊNIOR ")
else:
    print("Sua categoria é MASTER")


