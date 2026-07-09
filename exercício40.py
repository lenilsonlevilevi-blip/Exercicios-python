#Calcule as duas notas de um aluno

nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
media= (nota1 + nota2) /2
print(f"Sua média é {media:.2f}")

if media < 5:
    print("REPROVADO 😢")
elif media < 7:
    print("RECUPERAÇÃO 📚")
else:
    print("APROVADO 🎉")
