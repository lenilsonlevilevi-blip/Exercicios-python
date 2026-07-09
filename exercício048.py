# Soma números entre 1 e 500 que são múltiplos de 3 e ímpares
soma = 0
for c in range(1,501): #Pega números de 1 até 500
    if c % 3 == 0 and c % 2 == 1: #Filtra os que são divisíveis por 3 e ímpares
        print(c) #Mostra esses números
        soma = soma + c #somando todos eles
print(f"A soma é {soma}") #Mostra o resultado final
