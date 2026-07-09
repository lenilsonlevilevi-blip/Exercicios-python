num = int(input("Digite um número: "))
print("-" * 20)
print(f"  Tabuada de {num}")
print("-" * 20)
for c in range(1,11):
    print(f"{num:} x {c:} = {num * c}")