tupla= ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete","oito", "nove",
      "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
      "dezoito", "dezenove", "vinte")
num_digitado= int(input("Digite um número inteiro entre 0 e 20: "))

while num_digitado < 0 or num_digitado >20:
    num_digitado= int(input("Tente Novamente! Digite um número inteiro entre 0 e 20: "))
print(f"Você digitou o número {tupla[num_digitado]}")


