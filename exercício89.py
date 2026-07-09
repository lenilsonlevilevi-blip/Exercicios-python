alunos = []

while True:
    nome = str(input("nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2

    alunos.append([nome,n1,n2,media])

    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break

for i, n in enumerate(alunos):
    print(f"[{i}] Nome: {n[0]} | Média: {n[3]:.1f}")

while True:
    mostrar = int(input("Quer mostrar a notas de qual aluno? (999 para parar): "))
    if mostrar == 999:
        print("PROGRAMA FINALIZADO!")
        break

    print(f"Notas de {alunos[mostrar][0]} são: {alunos[mostrar][1]} | {alunos[mostrar][2]}")




