#Mostrando o maior número ou se são iguais
n1= int(input("Digite o primeiro valor: "))
n2= int(input("Digite o segundo valor: "))
if n1 > n2:
    print(f"O primeiro valor é o MAIOR: {n1}")
elif n2 > n1:
    print(f"O segundo valor é o MAIOR: {n2}")
else:
    print("Não existe valor maior, os dois são iguais")