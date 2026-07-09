termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 0
mais=0
total= 10
while contador!= 0:
    total += mais
    while contador < total:
        print(termo)
        termo += razao
        contador +=1
    while True:
        mais = int(input("Quer mais quantos termos: "))
        total += mais






