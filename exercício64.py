contador = 0
soma = 0
num = int(input("Digite um número inteiro [999] para parar: "))
while num !=999:
    contador +=1
    soma += num
    num = int(input("Digite um número inteiro [999] para parar: "))

print(f"foram digitados {contador} números e a soma entre eles é {soma}")

if contador > 0:
    media = soma / contador
    print(f"a média entre eles é {media:.2f}")
else:
    print("Nennhum número foi digitado.")








